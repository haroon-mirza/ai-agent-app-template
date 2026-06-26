from __future__ import annotations

from .domain_tools import build_tool_call
from .llm import generate_response
from .rag import retrieve_chunks
from .schemas import AgentAnswer


def route_question(question: str) -> str:
    return "general"


def run_graph(question: str) -> AgentAnswer:
    route_question(question)
    tool_call = build_tool_call(
        "example_tool",
        {"question": question},
        {"result": "placeholder"},
    )
    retrieved = retrieve_chunks(question)
    output = generate_response(question)
    return AgentAnswer(
        question=question,
        answer=output,
        sources=[chunk.source for chunk in retrieved if chunk.source],
        tool_calls=[tool_call],
    )
