from __future__ import annotations

from fastapi import FastAPI
from src.graph import run_graph

app = FastAPI(title="AI Agent App Template")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask")
def ask(question: str) -> dict[str, object]:
    answer = run_graph(question)
    return answer.model_dump()
