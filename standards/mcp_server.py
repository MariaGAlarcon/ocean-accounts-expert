#!/usr/bin/env python3
"""
MCP Server for Ocean Accounting Standards RAG System.
Exposes the document search functionality to Claude Desktop via the Model Context Protocol.
"""

import sys
import os
import asyncio
from pathlib import Path
from typing import Any
import chromadb
from sentence_transformers import SentenceTransformer
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Global variables for model and collection (loaded once on startup)
model = None
collection = None
chroma_client = None


def initialize_rag_system():
    """Initialize the embedding model and ChromaDB collection."""
    global model, collection, chroma_client

    try:
        # Load embedding model
        print("Loading embedding model...", file=sys.stderr)
        model = SentenceTransformer('all-MiniLM-L6-v2')
        print("Model loaded successfully", file=sys.stderr)

        # Load ChromaDB
        print("Loading ChromaDB...", file=sys.stderr)
        db_path = Path(__file__).parent / "chroma_db"

        if not db_path.exists():
            raise FileNotFoundError(
                f"ChromaDB not found at {db_path}. "
                "Please run ingest.py first to create the database."
            )

        chroma_client = chromadb.PersistentClient(path=str(db_path))
        collection = chroma_client.get_collection("standards_docs")
        print(f"ChromaDB loaded: {collection.count()} documents", file=sys.stderr)

    except Exception as e:
        print(f"Error initializing RAG system: {e}", file=sys.stderr)
        raise


def search_documents(query: str, top_k: int = 5) -> dict:
    """Search for relevant document chunks."""
    if model is None or collection is None:
        raise RuntimeError("RAG system not initialized")

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
        raise RuntimeError(f"Error searching documents: {e}")


def get_source_files() -> list:
    """Get a list of all unique source files in the database."""
    if collection is None:
        raise RuntimeError("RAG system not initialized")

    try:
        # Get all documents (we'll extract unique source files)
        all_data = collection.get()
        metadatas = all_data.get('metadatas', [])

        # Extract unique source files
        source_files = set()
        for meta in metadatas:
            if 'source_file' in meta:
                source_files.add(meta['source_file'])

        return sorted(list(source_files))
    except Exception as e:
        raise RuntimeError(f"Error getting source files: {e}")


# Create MCP server instance
app = Server("ocean-standards-rag")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools for Claude Desktop."""
    return [
        Tool(
            name="search_standards",
            description=(
                "Search the ocean accounting standards documents for relevant information. "
                "This tool performs semantic search across SEEA-EA, SEEA-CF, SNA25, and technical guidance documents. "
                "Returns the most relevant document chunks with their source file and section information. "
                "Use this to answer questions about ocean accounting standards, principles, methodology, and guidance."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query or question about ocean accounting standards"
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Number of results to return (default: 5, max: 10)",
                        "default": 5,
                        "minimum": 1,
                        "maximum": 10
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="list_standards",
            description=(
                "Get a list of all ocean accounting standards documents available in the database. "
                "Returns the filenames of all indexed documents. "
                "Use this to see what documents are available before searching."
            ),
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls from Claude Desktop."""
    try:
        if name == "search_standards":
            # Extract parameters
            query = arguments.get("query")
            if not query:
                return [TextContent(
                    type="text",
                    text="Error: 'query' parameter is required"
                )]

            top_k = arguments.get("top_k", 5)
            top_k = max(1, min(10, top_k))  # Clamp between 1 and 10

            # Perform search
            results = search_documents(query, top_k=top_k)

            # Format results
            documents = results['documents'][0]
            metadatas = results['metadatas'][0]

            if not documents:
                return [TextContent(
                    type="text",
                    text="No relevant documents found for your query."
                )]

            # Build response
            response_parts = [f"Found {len(documents)} relevant chunks:\n"]

            for i, (doc, meta) in enumerate(zip(documents, metadatas), 1):
                source_file = meta.get('source_file', 'Unknown')
                section = meta.get('section_header', 'Unknown section')
                chunk_idx = meta.get('chunk_index', '?')

                response_parts.append(f"\n--- Result {i} ---")
                response_parts.append(f"Source: {source_file}")
                response_parts.append(f"Section: {section}")
                response_parts.append(f"Chunk: {chunk_idx}")
                response_parts.append(f"\nContent:\n{doc}\n")

            return [TextContent(
                type="text",
                text="\n".join(response_parts)
            )]

        elif name == "list_standards":
            # Get list of source files
            source_files = get_source_files()

            if not source_files:
                return [TextContent(
                    type="text",
                    text="No documents found in the database."
                )]

            response = "Available ocean accounting standards documents:\n\n"
            for i, filename in enumerate(source_files, 1):
                response += f"{i}. {filename}\n"

            response += f"\nTotal: {len(source_files)} documents"

            return [TextContent(
                type="text",
                text=response
            )]

        else:
            return [TextContent(
                type="text",
                text=f"Error: Unknown tool '{name}'"
            )]

    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error executing tool '{name}': {str(e)}"
        )]


async def main():
    """Main entry point for the MCP server."""
    try:
        # Initialize RAG system on startup
        initialize_rag_system()

        # Run the server using stdio transport
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await app.run(
                read_stream,
                write_stream,
                app.create_initialization_options()
            )

    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
