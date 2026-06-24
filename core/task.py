from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Task:
    """
    Represents a unit of work routed between agents.

    A Task moves through the system from a source agent to a target agent.
    Agents may create new Tasks as follow‑ups or return lists of Tasks
    to extend the execution pipeline.
    """

    description: str
    source: str
    target: str

    depends_on: List[str] = field(default_factory=lambda: [])
    metadata: Dict[str, Any] = field(default_factory=lambda: {})
    context: Optional[Any] = None

    done: bool = False

    def mark_done(self) -> None:
        """Mark this task as completed."""
        self.done = True

    def is_ready(self, completed_tasks: List[str]) -> bool:
        """
        Check if this task can run based on dependencies.
        """
        return all(dep in completed_tasks for dep in self.depends_on)

    def __repr__(self) -> str:
        return (
            "Task("
            f"description={self.description!r}, "
            f"source={self.source!r}, "
            f"target={self.target!r}, "
            f"depends_on={self.depends_on!r}, "
            f"metadata={self.metadata!r}, "
            f"done={self.done}"
            ")"
        )
