from __future__ import annotations

from pathlib import Path

from .schemas import RetrievedChunk

DOCS_DIR = Path(__file__).resolve().parents[1] / "docs"


def load_markdown_docs(docs_dir: Path | None = None) -> list[tuple[str, str]]:
    base = docs_dir or DOCS_DIR
    if not base.exists():
        return []

    docs: list[tuple[str, str]] = []
    for path in sorted(base.glob("*.md")):
        docs.append((path.name, path.read_text(encoding="utf-8")))
    return docs


def retrieve_chunks(query: str, docs_dir: Path | None = None) -> list[RetrievedChunk]:
    docs = load_markdown_docs(docs_dir)
    if not docs:
        return []

    results: list[RetrievedChunk] = []
    for name, content in docs:
        if query.lower() in content.lower():
            results.append(RetrievedChunk(text=content[:400], source=name, score=0.5))
    return results
