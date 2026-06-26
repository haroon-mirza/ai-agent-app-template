from __future__ import annotations

import json
from pathlib import Path

from src.graph import run_graph

EVALS_PATH = Path(__file__).resolve().parent / "test_questions.jsonl"


def run_evals() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    with EVALS_PATH.open("r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            item = json.loads(line)
            answer = run_graph(item["question"])
            results.append({"question": item["question"], "answer": answer.answer})
    return results


if __name__ == "__main__":
    for item in run_evals():
        print(item)
