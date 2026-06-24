# core/project_context.py
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ProjectContext:
    """
    Shared project state used by agents during a Recuris build.

    This object acts as the central memory for a run. Agents read and
    update it as they plan architecture, generate code, and perform QA.
    """

    goal: str

    spec: Optional[str] = None
    architecture: Optional[str] = None

    filenames: List[str] = field(default_factory=lambda: [])
    code_snippets: List[str] = field(default_factory=lambda: [])

    qa_results: Dict[str, Dict[str, Any]] = field(default_factory=lambda: {})

    # agent-specific notes or decisions
    agent_notes: Dict[str, str] = field(default_factory=lambda: {})

    def update_spec(self, spec: str) -> None:
        """Store or replace the system specification."""
        self.spec = spec

    def update_architecture(self, architecture: str) -> None:
        """Store architecture decisions."""
        self.architecture = architecture

    def update_code(self, code: str) -> None:
        """Append a generated code snippet."""
        if code:
            self.code_snippets.append(code)

    def add_file(self, filename: str) -> None:
        """Register a generated file."""
        if filename not in self.filenames:
            self.filenames.append(filename)

    def add_qa_result(self, file: str, result: Dict[str, Any]) -> None:
        """Attach QA results to a file."""
        self.qa_results[file] = result

    def add_note(self, agent: str, note: str) -> None:
        """Allow agents to store reasoning or decisions."""
        self.agent_notes[agent] = note

    def get_agent_note(self, name: str) -> Optional[str]:
        """Retrieve notes left by a specific agent."""
        return self.agent_notes.get(name)

    def summary(self) -> Dict[str, Any]:
        """
        Return a lightweight summary of the project context.
        Useful for debugging or logging.
        """
        return {
            "goal": self.goal,
            "spec": bool(self.spec),
            "architecture": bool(self.architecture),
            "files": len(self.filenames),
            "code_snippets": len(self.code_snippets),
            "qa_results": len(self.qa_results),
        }
