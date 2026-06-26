from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class RetrievedChunk(BaseModel):
    text: str
    source: str | None = None
    score: float | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class ToolCallRecord(BaseModel):
    name: str
    inputs: dict[str, Any] = Field(default_factory=dict)
    outputs: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AgentState(BaseModel):
    question: str
    intent: str = "general"
    retrieved_chunks: list[RetrievedChunk] = Field(default_factory=list)
    tool_calls: list[ToolCallRecord] = Field(default_factory=list)
    answer: str | None = None
    error: str | None = None


class AgentAnswer(BaseModel):
    question: str
    answer: str
    sources: list[str] = Field(default_factory=list)
    tool_calls: list[ToolCallRecord] = Field(default_factory=list)


class EvalQuestion(BaseModel):
    question: str
    expected_intent: str
    expected_tools: list[str] = Field(default_factory=list)
    expected_docs: list[str] = Field(default_factory=list)
    expected_answer_notes: list[str] = Field(default_factory=list)


class LogRecord(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    question: str
    model: str | None = None
    tool_calls: list[ToolCallRecord] = Field(default_factory=list)
    retrieved_chunks: list[RetrievedChunk] = Field(default_factory=list)
    latency_ms: int | None = None
    errors: list[str] = Field(default_factory=list)
    final_answer: str | None = None
