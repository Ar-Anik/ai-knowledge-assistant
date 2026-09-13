# AI Knowledge Assistant

Built a **RAG (Retrieval-Augmented Generation)** project built with **FastAPI, Gemini API, Gemini Embeddings and ChromaDB**.

## Architecture

```text
DOCUMENT INDEXING

Document
   ↓
Load
   ↓
Chunking
   ↓
Gemini Embedding
   ↓
Vector
   ↓
ChromaDB
```

```text
QUESTION ANSWERING

User Question
      ↓
FastAPI
      ↓
Question Embedding
      ↓
ChromaDB Similarity Search
      ↓
Relevant Chunks
      ↓
Question + Context
      ↓
Gemini LLM
      ↓
Generated Answer
      ↓
FastAPI Response
```

## Technologies

* **FastAPI** — REST API
* **Gemini Embedding Model** — text → vector
* **Gemini 3.7 Flash** — answer generation
* **ChromaDB** — vector storage and similarity search
* **Pydantic** — request/response validation
* **python-dotenv** — environment variables

## Project Structure

```text
ai-knowledge-assistant/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── llm.py
│   ├── rag.py
│   └── schemas.py
│
├── data/
│   └── company_policy.txt
│
├── chroma_db/
├── requirements.txt
└── .env
```

## File Responsibilities

### `main.py`

FastAPI application and API endpoints.

```text
GET  /
POST /index
POST /ask
```

### `llm.py`

Handles Gemini operations:

```text
embed_content()
→ creates embeddings

generate_content()
→ generates final answer
```

### `rag.py`

Contains the main RAG pipeline:

```text
Load document
→ Chunk document
→ Create embeddings
→ Store in ChromaDB
→ Search relevant chunks
→ Send context to Gemini
→ Return answer
```

### `schemas.py`

Pydantic request/response models.

### `data/company_policy.txt`

Knowledge source used by the RAG system.

### `chroma_db/`

Local persistent ChromaDB data.

### `.env`

Stores the Gemini API key.

```env
GEMINI_API_KEY=your_api_key
```

## Setup

Create and activate virtual environment:

```bash
python -m venv aienv
source aienv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Usage

### 1. Index document

Call:

```text
POST /index
```

This performs:

```text
Document
→ Chunks
→ Embeddings
→ ChromaDB
```

### 2. Ask question

Call:

```text
POST /ask
```

Request:

```json
{
    "question": "How many annual leave days do employees receive?"
}
```

Flow:

```text
Question
→ Embedding
→ Similarity Search
→ Relevant Context
→ Gemini
→ Answer
```

Example response:

```json
{
    "answer": "Employees receive 20 annual leave days every year."
}
```

## Core RAG Flow

```text
INDEX

Document
  ↓
Chunk
  ↓
Embedding
  ↓
ChromaDB


QUERY

Question
  ↓
Embedding
  ↓
Similarity Search
  ↓
Relevant Chunks
  ↓
Context + Question
  ↓
Gemini
  ↓
Answer
```

## Key Components

```text
FastAPI
→ API layer

Gemini Embedding
→ Text to vector

ChromaDB
→ Store and search vectors

Gemini LLM
→ Generate answer

RAG
→ Retrieve relevant information before generation
```

## Important Distinction

Gemini has two different operations in this project:

```python
gemini_client.models.embed_content(...)
```

Used for:

```text
Text → Vector
```

and:

```python
gemini_client.models.generate_content(...)
```

Used for:

```text
Question + Context → Answer
```

