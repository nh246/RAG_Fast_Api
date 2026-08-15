# Project 01: FastAPI RAG Chatbot

A production-grade Retrieval-Augmented Generation (RAG) system built over the FastAPI official documentation.

## Day 1: Ingestion Pipeline

### Dataset
- **Source:** [FastAPI official docs](https://github.com/tiangolo/fastapi)
- **Format:** Markdown (`.md`)
- **Count:** 155 files
- **Location:** `data/raw/`

### Chunking Strategy
- **Chunk size:** 500 characters
- **Overlap:** 50 characters
- **Rationale:** Balances context preservation with retrieval granularity. Overlap ensures sentences crossing chunk boundaries appear in both chunks.

### Cleaning Steps
- Stripped YAML frontmatter (`---`)
- Removed markdown headers (`#`, `##`, etc.)
- Removed bold (`**`) and italic (`_`) markers
- Removed link URLs (kept link text)
- Removed code block fences (kept code content)
- Removed MkDocs anchor syntax (`{ #... }`)

### Output
- **Total chunks:** 2,476
- **Saved to:** `data/processed/chunks.json`
- **Schema:** `{"source": "filename.md", "chunk_index": 0, "content": "..."}`

### Run the Pipeline
```bash
python src/ingest.py
