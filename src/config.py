from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env", override=False)

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "ollama")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:4b")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
VECTOR_STORE_PATH = Path(os.getenv("VECTOR_STORE_PATH", str(ROOT / "vector_store" / "chroma")))
LOG_PATH = Path(os.getenv("LOG_PATH", str(ROOT / "logs" / "agent_runs.jsonl")))
