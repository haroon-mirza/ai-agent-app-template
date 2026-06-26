from __future__ import annotations

import json

from .config import LOG_PATH
from .schemas import LogRecord


def append_log(record: LogRecord) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record.model_dump(), default=str) + "\n")


def log_run(question: str, answer: str, latency_ms: int | None = None) -> None:
    record = LogRecord(question=question, final_answer=answer, latency_ms=latency_ms)
    append_log(record)
