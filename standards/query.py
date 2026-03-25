#!/usr/bin/env python3
"""
Query the ocean accounting standards RAG system.
Takes a question as command line argument and returns an answer with sources.
"""

import os
import sys
import chromadb
from sentence_transformers import SentenceTransformer
from anthropic import Anthropic
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def load_chroma_collection():
    """Load the ChromaDB collection."""
    try:
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_collection("standards_docs")
        return collection
    except Exception as e:
        console.print(f"[red]❌ Error loading ChromaDB: {e}[/red]")
        console.print("[yellow]💡 Have you run ingest.py first?[/yellow]")
        sys.exit(1)


def search_documents(collection, model, query: str, top_k: int = 5):
    """Search for relevant document chunks."""
    try:
        # Create query embedding
        query_embedding = model.encode(query).tolist()

        # Search in ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results
    except Exception as e:
        console.print(f"[red]❌ Error searching documents: {e}[/red]")
        sys.exit(1)


def build_prompt(query: str, results) -> str:
    """Build the prompt for Claude with context from retrieved chunks."""
    context_parts = []

    documents = results['documents'][0]
    metadatas = results['metadatas'][0]

    for i, (doc, meta) in enumerate(zip(documents, metadatas), 1):
        source = meta.get('source_file', 'Unknown')
        section = meta.get('section_header', 'Unknown section')

        context_parts.append(
            f"[Source {i}: {source} - {section}]\n{doc}\n"
        )

    context = "\n---\n\n".join(context_parts)

    prompt = f"""You are an expert assistant helping users understand ocean accounting standards. You have been provided with relevant excerpts from technical documentation.

Based on the following context from the standards documentation, please answer the user's question. Be specific and cite which source(s) you're drawing from when relevant.

CONTEXT:
{context}

USER QUESTION:
{query}

Please provide a clear, accurate answer based on the context provided. If the context doesn't contain enough information to fully answer the question, acknowledge this."""

    return prompt


def query_claude(prompt: str, api_key: str) -> str:
    """Query Claude API with the prompt."""
    try:
        client = Anthropic(api_key=api_key)

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return message.content[0].text
    except Exception as e:
        console.print(f"[red]❌ Error calling Claude API: {e}[/red]")
        console.print("[yellow]💡 Check your ANTHROPIC_API_KEY environment variable[/yellow]")
        sys.exit(1)


def format_sources(results):
    """Format source information for display."""
    sources = []
    metadatas = results['metadatas'][0]

    for i, meta in enumerate(metadatas, 1):
        source_file = meta.get('source_file', 'Unknown')
        section = meta.get('section_header', 'Unknown section')
        chunk_idx = meta.get('chunk_index', '?')

        sources.append(f"{i}. {source_file} - {section} (chunk {chunk_idx})")

    return sources


def main():
    """Main query function."""
    # Check for query argument
    if len(sys.argv) < 2:
        console.print("[red]❌ Usage: python query.py \"your question here\"[/red]")
        sys.exit(1)

    query = " ".join(sys.argv[1:])

    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]❌ ANTHROPIC_API_KEY environment variable not set[/red]")
        console.print("[yellow]💡 Set it with: export ANTHROPIC_API_KEY='your-key-here'[/yellow]")
        sys.exit(1)

    console.print(Panel.fit(
        "[bold cyan]Ocean Accounting Standards - RAG Query[/bold cyan]",
        border_style="cyan"
    ))

    console.print(f"\n[yellow]Question:[/yellow] {query}\n")

    # Load embedding model
    console.print("[dim]Loading embedding model...[/dim]")
    try:
        model = SentenceTransformer('all-MiniLM-L6-v2')
    except Exception as e:
        console.print(f"[red]❌ Error loading model: {e}[/red]")
        sys.exit(1)

    # Load ChromaDB collection
    console.print("[dim]Loading document database...[/dim]")
    collection = load_chroma_collection()

    # Search for relevant documents
    console.print("[dim]Searching for relevant content...[/dim]")
    results = search_documents(collection, model, query, top_k=5)

    # Build prompt
    prompt = build_prompt(query, results)

    # Query Claude
    console.print("[dim]Querying Claude API...[/dim]\n")
    answer = query_claude(prompt, api_key)

    # Display answer
    console.print(Panel(
        Markdown(answer),
        title="[bold green]Answer[/bold green]",
        border_style="green",
        padding=(1, 2)
    ))

    # Display sources
    console.print("\n[bold cyan]📚 Sources Used:[/bold cyan]")
    sources = format_sources(results)
    for source in sources:
        console.print(f"  {source}")
    console.print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Query cancelled by user[/yellow]")
        sys.exit(0)
