from __future__ import annotations

from .config import OLLAMA_MODEL


def generate_response(prompt: str, model: str | None = None) -> str:
    """Return a placeholder response for local-first development."""
    selected_model = model or OLLAMA_MODEL
    return f"[local:{selected_model}] {prompt[:200]}"
