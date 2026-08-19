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

## Day 2 — Embeddings + Vector Store

**Model:** all-MiniLM-L6-v2 (free, local, ONNX via ChromaDB's default embedding function).
**Why:** no GPU on my machine, $0 cost, and MiniLM (~90 MB) is strong enough for a
single-topic technical corpus. I'll upgrade to OpenAI text-embedding-3-small ONLY if
Day 5 evals show retrieval quality is the bottleneck.

**Pipeline:** src/embed.py loads Day 1's chunks.json, embeds each chunk (384-dim
vectors), and stores text + vector + metadata (source, chunk_index) into a local
ChromaDB collection `fastapi_docs` (data/chroma_db).

**Results:** 2,476 chunks embedded + stored. Run time: ~X min on CPU.
(Local note: chromadb's ONNX model cache patched to E: drive — C: drive is full.)

**Retrieval:** src/retrieve.py embeds the query with the SAME model and returns
top-k (k=5) chunks ranked by distance.

**10-query sanity check (src/sanity_check.py):**
- Strong hits: dependency injection, CORS, OAuth2, JSON responses, deploy,
  background tasks, request validation ✅
