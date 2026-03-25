#!/usr/bin/env python3
"""
Ingest markdown documents into ChromaDB for RAG search.
Processes .md files, creates embeddings, and stores them with metadata.
"""

import os
import re
import glob
from pathlib import Path
from typing import List, Dict, Tuple
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel
from rich.table import Table

console = Console()


def find_markdown_files() -> List[str]:
    """Find all .md files in current directory, excluding README.md."""
    # Use Path for better handling of special characters
    current_dir = Path(".")
    md_files = []

    # Find all .md files using pathlib
    for file_path in current_dir.glob("*.md"):
        filename = file_path.name
        # Exclude README.md (case-insensitive)
        if filename.lower() != "readme.md":
            md_files.append(filename)

    return sorted(md_files)


def extract_headers(text: str) -> List[Tuple[int, str, str]]:
    """
    Extract markdown headers with their positions.
    Returns list of (position, level, header_text) tuples.
    """
    headers = []
    pattern = r'^(#{1,6})\s+(.+)$'

    for match in re.finditer(pattern, text, re.MULTILINE):
        level = len(match.group(1))
        header_text = match.group(2).strip()
        position = match.start()
        headers.append((position, level, header_text))

    return headers


def approximate_tokens(text: str) -> int:
    """Approximate token count (rough estimate: 1 token ≈ 4 characters)."""
    return len(text) // 4


def split_into_chunks(text: str, source_file: str, target_tokens: int = 500) -> List[Dict[str, str]]:
    """
    Split text into chunks respecting markdown headers.
    Each chunk aims for ~target_tokens tokens.
    """
    chunks = []
    headers = extract_headers(text)

    if not headers:
        # No headers found, split by simple token count
        return split_by_tokens(text, source_file, target_tokens)

    # Add end position for easier slicing
    headers.append((len(text), 0, ""))

    current_header_stack = []

    for i in range(len(headers) - 1):
        pos, level, header_text = headers[i]
        next_pos = headers[i + 1][0]

        # Update header stack based on level
        current_header_stack = [h for h in current_header_stack if h[0] < level]
        current_header_stack.append((level, header_text))

        # Extract section content (from after header to next header)
        section_start = pos
        section_end = next_pos
        section_text = text[section_start:section_end].strip()

        # Build full header path (e.g., "Chapter 1 > Section 1.1 > Subsection")
        header_path = " > ".join([h[1] for h in current_header_stack])

        # If section is too large, split it further
        section_tokens = approximate_tokens(section_text)

        if section_tokens > target_tokens * 1.5:
            # Split large section into smaller chunks
            sub_chunks = split_by_tokens(section_text, source_file, target_tokens, header_path)
            chunks.extend(sub_chunks)
        else:
            # Keep section as single chunk
            if section_text:
                chunks.append({
                    "text": section_text,
                    "source_file": source_file,
                    "section_header": header_path,
                })

    return chunks


def split_by_tokens(text: str, source_file: str, target_tokens: int = 500,
                   section_header: str = "") -> List[Dict[str, str]]:
    """Split text into chunks by approximate token count."""
    chunks = []
    target_chars = target_tokens * 4  # Rough approximation

    # Split by paragraphs first
    paragraphs = text.split('\n\n')

    current_chunk = ""
    for para in paragraphs:
        if not para.strip():
            continue

        if len(current_chunk) + len(para) < target_chars:
            current_chunk += para + "\n\n"
        else:
            if current_chunk.strip():
                chunks.append({
                    "text": current_chunk.strip(),
                    "source_file": source_file,
                    "section_header": section_header or "Main content",
                })
            current_chunk = para + "\n\n"

    # Add remaining chunk
    if current_chunk.strip():
        chunks.append({
            "text": current_chunk.strip(),
            "source_file": source_file,
            "section_header": section_header or "Main content",
        })

    return chunks


def ingest_documents():
    """Main ingestion function."""
    console.print(Panel.fit(
        "[bold cyan]Ocean Accounting Standards - Document Ingestion[/bold cyan]",
        border_style="cyan"
    ))

    # Find markdown files
    console.print("\n[yellow]🔍 Searching for markdown files...[/yellow]")
    md_files = find_markdown_files()

    if not md_files:
        console.print("[red]❌ No markdown files found in current directory![/red]")
        return

    console.print(f"[green]✓ Found {len(md_files)} file(s):[/green]")
    for f in md_files:
        console.print(f"  • {f}")

    # Initialize embedding model
    console.print("\n[yellow]🤖 Loading embedding model (all-MiniLM-L6-v2)...[/yellow]")
    try:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        console.print("[green]✓ Model loaded successfully[/green]")
    except Exception as e:
        console.print(f"[red]❌ Failed to load model: {e}[/red]")
        return

    # Initialize ChromaDB
    console.print("\n[yellow]💾 Initializing ChromaDB...[/yellow]")
    try:
        client = chromadb.PersistentClient(path="./chroma_db")

        # Delete existing collection if it exists
        try:
            client.delete_collection("standards_docs")
        except:
            pass

        collection = client.create_collection(
            name="standards_docs",
            metadata={"description": "Ocean accounting standards documents"}
        )
        console.print("[green]✓ ChromaDB initialized[/green]")
    except Exception as e:
        console.print(f"[red]❌ Failed to initialize ChromaDB: {e}[/red]")
        return

    # Process documents
    console.print("\n[yellow]📄 Processing documents...[/yellow]")

    all_chunks = []
    total_chunks = 0
    processed_files = []
    skipped_files = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:

        task = progress.add_task("[cyan]Processing files...", total=len(md_files))

        for md_file in md_files:
            try:
                # Use Path for robust file handling with special characters
                file_path = Path(md_file)

                # Check if file exists and is readable
                if not file_path.exists():
                    console.print(f"[yellow]⚠ File not found: {md_file}[/yellow]")
                    skipped_files.append((md_file, "File not found"))
                    progress.update(task, advance=1)
                    continue

                # Read file with explicit encoding
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()

                # Check if file is empty
                if not content.strip():
                    console.print(f"[yellow]⚠ Empty file skipped: {md_file}[/yellow]")
                    skipped_files.append((md_file, "Empty file"))
                    progress.update(task, advance=1)
                    continue

                # Split into chunks
                chunks = split_into_chunks(content, md_file)

                # Check if chunks were created
                if not chunks:
                    console.print(f"[yellow]⚠ No chunks created for: {md_file}[/yellow]")
                    skipped_files.append((md_file, "No chunks created"))
                    progress.update(task, advance=1)
                    continue

                # Add chunk index
                for idx, chunk in enumerate(chunks):
                    chunk['chunk_index'] = idx

                all_chunks.extend(chunks)
                total_chunks += len(chunks)
                processed_files.append((md_file, len(chunks)))

                progress.update(task, advance=1,
                              description=f"[cyan]Processed {md_file} ({len(chunks)} chunks)")

            except UnicodeDecodeError as e:
                console.print(f"[red]❌ Encoding error in {md_file}: {e}[/red]")
                skipped_files.append((md_file, f"Encoding error: {e}"))
                progress.update(task, advance=1)
            except PermissionError as e:
                console.print(f"[red]❌ Permission denied: {md_file}[/red]")
                skipped_files.append((md_file, "Permission denied"))
                progress.update(task, advance=1)
            except Exception as e:
                console.print(f"[red]❌ Error processing {md_file}: {e}[/red]")
                skipped_files.append((md_file, str(e)))
                progress.update(task, advance=1)

    console.print(f"[green]✓ Processed {len(processed_files)} files into {total_chunks} chunks[/green]")

    # Show detailed processing results
    if processed_files:
        console.print("\n[bold cyan]Successfully Processed:[/bold cyan]")
        for filename, chunk_count in processed_files:
            console.print(f"  [green]✓[/green] {filename} → {chunk_count} chunks")

    if skipped_files:
        console.print("\n[bold yellow]Skipped Files:[/bold yellow]")
        for filename, reason in skipped_files:
            console.print(f"  [yellow]⚠[/yellow] {filename} - {reason}")

    # Create embeddings and store in ChromaDB
    console.print("\n[yellow]🔮 Creating embeddings and storing in database...[/yellow]")

    batch_size = 100
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:

        task = progress.add_task("[cyan]Creating embeddings...", total=len(all_chunks))

        for i in range(0, len(all_chunks), batch_size):
            batch = all_chunks[i:i + batch_size]

            try:
                # Extract texts
                texts = [chunk['text'] for chunk in batch]

                # Create embeddings
                embeddings = model.encode(texts, show_progress_bar=False)

                # Prepare for ChromaDB
                ids = [f"chunk_{i + j}" for j in range(len(batch))]
                metadatas = [
                    {
                        "source_file": chunk['source_file'],
                        "section_header": chunk['section_header'],
                        "chunk_index": chunk['chunk_index']
                    }
                    for chunk in batch
                ]

                # Add to collection
                collection.add(
                    ids=ids,
                    embeddings=embeddings.tolist(),
                    documents=texts,
                    metadatas=metadatas
                )

                progress.update(task, advance=len(batch))

            except Exception as e:
                console.print(f"[red]❌ Error creating embeddings for batch: {e}[/red]")
                progress.update(task, advance=len(batch))

    # Print summary
    console.print("\n" + "="*60)
    console.print(Panel.fit(
        "[bold green]✓ Ingestion Complete![/bold green]",
        border_style="green"
    ))

    # Create summary table
    table = Table(title="Ingestion Summary", show_header=True, header_style="bold cyan")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Files Found", str(len(md_files)))
    table.add_row("Files Processed", str(len(processed_files)))
    table.add_row("Files Skipped", str(len(skipped_files)), style="yellow" if skipped_files else "green")
    table.add_row("Total Chunks", str(total_chunks))
    table.add_row("Database Location", "./chroma_db")
    table.add_row("Embedding Model", "all-MiniLM-L6-v2")

    console.print(table)
    console.print()


if __name__ == "__main__":
    try:
        ingest_documents()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Ingestion cancelled by user[/yellow]")
    except Exception as e:
        console.print(f"\n[red]❌ Fatal error: {e}[/red]")
        raise
