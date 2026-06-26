# AI Agent Template

A starter template for building AI apps with tool calling, RAG, APIs, basic UI, tests, and observability.

The goal is to have a clean base for AI projects.

## What this includes

* Python 3.12 project setup
* Dependency management with uv
* Linting and formatting with ruff
* Testing with pytest
* FastAPI backend structure
* Streamlit UI structure
* Pydantic schemas
* Local LLM support through Ollama
* RAG support with Chroma
* Local data access with pandas and DuckDB
* Evaluation folder for test questions
* JSONL logging structure

## Stack

* Python 3.12
* uv
* pandas
* DuckDB
* FastAPI
* Streamlit
* Pydantic
* Pydantic AI
* Ollama
* Chroma
* Sentence Transformers or Ollama embeddings
* pytest
* ruff

## Project structure

'''text
local-ai-agent-template/
├── app/
│   ├── api.py
│   └── ui_streamlit.py
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── tools.py
│   ├── rag.py
│   ├── llm.py
│   ├── prompts.py
│   ├── orchestrator.py
│   ├── schemas.py
│   └── logging_utils.py
├── data/
├── docs/
├── vector_store/
│   └── chroma/
├── evals/
│   ├── test_questions.jsonl
│   └── run_evals.py
├── tests/
│   └── test_setup.py
├── pyproject.toml
└── README.md
'''

## Notes

This template is intentionally minimal

## Template usage

This repository is marked as a GitHub template. For guidance, see [TEMPLATE.md](TEMPLATE.md).

To create a new repository from this template using the GitHub CLI:

```bash
gh repo create <new-repo-name> --template haroon-mirza/ai-agent-app-template
```

After creating a new repository from this template, update the project `README.md`, repository name, and repository secrets as needed.