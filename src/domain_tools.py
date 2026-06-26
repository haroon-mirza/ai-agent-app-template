from __future__ import annotations

from .schemas import ToolCallRecord


def example_tool(question: str) -> dict[str, object]:
    """Return a safe placeholder result for a generic domain tool."""
    return {"question": question, "result": "No domain-specific tool output configured yet."}


def build_tool_call(
    name: str,
    inputs: dict[str, object],
    outputs: dict[str, object],
) -> ToolCallRecord:
    return ToolCallRecord(name=name, inputs=inputs, outputs=outputs)
