# Ocean Accounting Standards - RAG Search System

A Retrieval-Augmented Generation (RAG) system for searching and querying ocean accounting technical standards documents using ChromaDB, sentence transformers, and Claude AI.

## Overview

This system allows you to:
- Ingest large markdown technical documents into a vector database
- Search documents using semantic similarity
- Get AI-powered answers to questions with source citations
- Interactive chat mode for multiple queries
- Connect directly to Claude Desktop via MCP (Model Context Protocol)

## Prerequisites

- Python 3.8 or higher
- An Anthropic API key ([get one here](https://console.anthropic.com/))

## Installation

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

This will install:
- `chromadb` - Vector database for storing document embeddings
- `sentence-transformers` - For creating document embeddings
- `anthropic` - Claude AI API client
- `rich` - Beautiful terminal formatting
- `mcp` - Model Context Protocol SDK for Claude Desktop integration

2. **Set up your API key**

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

For persistent setup, add this to your `~/.bashrc` or `~/.zshrc`:

```bash
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Usage

### Step 1: Ingest Documents

First, process your markdown documents and create the vector database:

```bash
python ingest.py
```

This will:
- Find all `.md` files in the current directory (excluding README.md)
- Split documents into ~500 token chunks while respecting markdown headers
- Create embeddings using the `all-MiniLM-L6-v2` model
- Store everything in a `chroma_db` folder

**Expected output:**
```
🔍 Searching for markdown files...
✓ Found 5 file(s):
  • SEEA-EA.md
  • SEEA-CF.md
  • SNA25.md
  • Technical guidance OA.md
  ...

🤖 Loading embedding model...
✓ Model loaded successfully

💾 Initializing ChromaDB...
✓ ChromaDB initialized

📄 Processing documents...
✓ Processed 5 files into 342 chunks

🔮 Creating embeddings and storing in database...
✓ Ingestion Complete!
```

### Step 2: Query the System

#### Single Query Mode

Ask a single question:

```bash
python query.py "What are the key principles of ocean accounting?"
```

**Example output:**
```
Question: What are the key principles of ocean accounting?

┌─ Answer ─────────────────────────────────────┐
│ The key principles of ocean accounting       │
│ include...                                    │
│                                              │
│ [Detailed answer from Claude]                │
└──────────────────────────────────────────────┘

📚 Sources Used:
  1. SEEA-EA.md - Chapter 2 > Principles (chunk 5)
  2. Technical guidance OA.md - Introduction > Core concepts (chunk 2)
  ...
```

#### Interactive Chat Mode

Start an interactive session:

```bash
python chat.py
```

This enters a chat loop where you can ask multiple questions:

```
Your question: What is ecosystem accounting?
[Answer with sources]

Your question: How does it differ from national accounting?
[Answer with sources]

Your question: quit
👋 Goodbye!
```

Type `quit`, `exit`, or `q` to end the session.

### Step 3: Use with Claude Desktop (MCP Integration)

You can connect this RAG system directly to Claude Desktop using the Model Context Protocol (MCP). This allows Claude to search your standards documents directly without needing API keys or running separate scripts.

#### Installation

1. **Install the MCP package** (if not already installed):

```bash
pip install -r requirements.txt
```

2. **Make sure you've ingested your documents**:

```bash
python ingest.py
```

3. **Configure Claude Desktop**:

On Mac, edit your Claude Desktop configuration file:

```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Or open it manually at:
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

Add the following configuration (see [claude_desktop_config.json](claude_desktop_config.json) for the template):

```json
{
  "mcpServers": {
    "ocean-standards-rag": {
      "command": "python3",
      "args": [
        "/Users/mariaalarcon/Desktop/standards/mcp_server.py"
      ],
      "env": {}
    }
  }
}
```

**Important**: Replace `/Users/mariaalarcon/Desktop/standards/mcp_server.py` with the actual absolute path to your `mcp_server.py` file.

4. **Restart Claude Desktop**

After saving the configuration, completely quit and restart Claude Desktop.

#### Available MCP Tools

Once configured, Claude Desktop will have access to two tools:

1. **search_standards** - Search the ocean accounting standards documents
   - Takes a query string
   - Returns top 5 relevant chunks with source information
   - Example: "search for principles of ocean accounting"

2. **list_standards** - List all available documents
   - No parameters needed
   - Returns a list of all indexed document files

#### Example Usage in Claude Desktop

Simply ask Claude questions like:

```
"Can you search the standards for information about ecosystem accounting?"

"What documents do you have available? Then search for ocean valuation methods."

"Search the standards for guidance on measuring ocean health."
```

Claude will automatically use the MCP tools to search your local document database and provide answers based on the actual content of your standards documents.

#### Troubleshooting MCP

**"Tool not showing up"**
- Check that the path in `claude_desktop_config.json` is absolute (not relative)
- Verify the path exists: `ls /path/to/your/mcp_server.py`
- Make sure you completely quit and restarted Claude Desktop

**"Error loading ChromaDB"**
- Ensure you've run `python ingest.py` first
- Check that `chroma_db` folder exists in the same directory as `mcp_server.py`

**"MCP server crashed"**
- Test the server manually: `python3 mcp_server.py`
- Check Claude Desktop logs (Help → View Logs)

**"Module not found: mcp"**
- Install dependencies: `pip install -r requirements.txt`
- Verify installation: `python3 -c "import mcp; print('MCP installed')"`

## File Structure

```
.
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
├── ingest.py                        # Document ingestion script
├── query.py                         # Single query mode
├── chat.py                          # Interactive chat mode
├── mcp_server.py                    # MCP server for Claude Desktop
├── claude_desktop_config.json       # Claude Desktop configuration template
├── chroma_db/                       # Vector database (created by ingest.py)
├── SEEA-EA.md                       # Your standard documents
├── SEEA-CF.md
├── SNA25.md
├── Technical guidance OA.md
└── ...                              # Other .md files
```

## How It Works

1. **Document Processing** (`ingest.py`)
   - Scans for markdown files
   - Intelligently splits text at markdown headers
   - Maintains context with section headers
   - Creates 384-dimensional embeddings for each chunk
   - Stores in ChromaDB with metadata

2. **Query Processing** (`query.py`, `chat.py`)
   - Converts your question to an embedding
   - Finds the 5 most semantically similar document chunks
   - Constructs a prompt with relevant context
   - Sends to Claude Sonnet 4 for answer generation
   - Returns answer with source citations

## Configuration

### Adjusting Chunk Size

Edit `ingest.py`, line ~75:

```python
chunks = split_into_chunks(content, md_file, target_tokens=500)  # Change 500 to your preferred size
```

### Changing Number of Retrieved Chunks

Edit `query.py` or `chat.py`, search function call:

```python
results = search_documents(collection, model, query, top_k=5)  # Change 5 to preferred number
```

### Using a Different Claude Model

Edit `query.py` or `chat.py`, model parameter:

```python
message = client.messages.create(
    model="claude-sonnet-4-20250514",  # Change to another model
    max_tokens=2048,
    ...
)
```

Available models:
- `claude-sonnet-4-20250514` (recommended, balanced)
- `claude-opus-4-5-20251101` (most capable, slower)
- `claude-sonnet-3-5-20241022` (faster, cheaper)

## Troubleshooting

### "No markdown files found"
- Ensure you have `.md` files in the current directory
- Check that they're not named `README.md` (excluded by default)

### "Error loading ChromaDB: Collection not found"
- Run `python ingest.py` first to create the database

### "ANTHROPIC_API_KEY environment variable not set"
- Set your API key: `export ANTHROPIC_API_KEY='your-key'`
- Verify: `echo $ANTHROPIC_API_KEY`

### "Error loading model"
- Check internet connection (first run downloads the model)
- Ensure enough disk space (~100MB for the model)

### Database corruption
- Delete the `chroma_db` folder and re-run `ingest.py`

```bash
rm -rf chroma_db
python ingest.py
```

## Advanced Usage

### Re-ingesting Documents

If you modify your markdown files:

```bash
python ingest.py
```

This will recreate the database with updated content.

### Querying Specific Documents

The system automatically searches all ingested documents. To limit to specific files, you would need to filter results by the `source_file` metadata field (requires code modification).

### Batch Queries

Create a file with questions and loop through them:

```bash
while IFS= read -r question; do
  python query.py "$question"
done < questions.txt
```

## Performance Notes

- Initial model download: ~100MB, one-time
- Ingestion speed: ~50-100 chunks/second
- Query speed: ~2-3 seconds per question
- Database size: ~1-2MB per 100 document chunks

## License

This is a utility tool for working with ocean accounting standards documentation.

## Support

For issues or questions about:
- The RAG system: Review this README and check error messages
- Ocean accounting standards: Refer to the official documentation
- Claude API: Visit [docs.anthropic.com](https://docs.anthropic.com)
