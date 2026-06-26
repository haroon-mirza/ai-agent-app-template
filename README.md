# AI Agent App Template

This repository is a starter for building agentic RAG applications with a local-first workflow. It is designed for projects that combine document retrieval, structured tools, and grounded LLM responses.

## What is included

- FastAPI backend
- Streamlit UI
- Pydantic schemas
- LangGraph workflow skeleton
- LlamaIndex RAG setup
- Chroma vector store
- Ollama-based local model support
- DuckDB and pandas for structured analysis
- pytest and ruff
- JSONL logging

## How to use it

1. Copy this repository into a new project folder.
2. Add domain-specific data sources and tools.
3. Replace the placeholder examples in the tool and RAG modules.
4. Update prompts, docs, and eval questions for your domain.

## Run checks

```bash
uv run ruff check .
uv run pytest -q
```

## Notes

The template is intentionally minimal. It leaves room for domain-specific retrieval, workflow logic, and evaluation.
