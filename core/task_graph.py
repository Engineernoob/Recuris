from __future__ import annotations

from typing import Dict, List, Optional

from core.task import Task


class TaskGraph:
    """
    Tracks task dependencies and determines which tasks are ready to run.

    Nodes are stored by task ID, and edges map each dependency to the tasks
    that depend on it.
    """

    def __init__(self):
        self.nodes: Dict[str, Task] = {}
        self.edges: Dict[str, List[str]] = {}

    def _get_task_id(self, task: Task, task_id: Optional[str] = None) -> str:
        """Resolve a stable task identifier."""
        if task_id:
            return str(task_id)

        meta_task_id = (
            task.metadata.get("task_id") if hasattr(task, "metadata") else None
        )
        if meta_task_id:
            return str(meta_task_id)

        return str(task.description)

    def add_task(self, task: Task, task_id: Optional[str] = None) -> str:
        """
        Add a task to the graph and register its dependencies.
        Returns the resolved task ID.
        """
        resolved_id = self._get_task_id(task, task_id)
        self.nodes[resolved_id] = task
        self.edges.setdefault(resolved_id, [])

        for dep in getattr(task, "depends_on", []):
            if isinstance(dep, dict):
                print(f"⚠️ Skipping invalid dependency (dict): {dep}")
                continue

            dep_id = str(dep)
            self.edges.setdefault(dep_id, [])

            if resolved_id not in self.edges[dep_id]:
                self.edges[dep_id].append(resolved_id)

        return resolved_id

    def mark_done(self, task_id: str) -> None:
        """Mark a task as completed if it exists."""
        task = self.nodes.get(task_id)
        if task:
            task.mark_done()

    def get_task(self, task_id: str) -> Optional[Task]:
        """Return a task by ID if present."""
        return self.nodes.get(task_id)

    def get_ready_tasks(self) -> List[Task]:
        """
        Return all tasks whose dependencies have been completed.
        Tasks with no dependencies are considered ready.
        """
        ready: List[Task] = []

        for _, task in self.nodes.items():
            if task.done:
                continue

            deps = getattr(task, "depends_on", [])
            if all(
                self.nodes.get(str(dep)) and self.nodes[str(dep)].done for dep in deps
            ):
                ready.append(task)

        return ready

    def all_tasks(self) -> List[Task]:
        """Return all tracked tasks."""
        return list(self.nodes.values())

    def pending_tasks(self) -> List[Task]:
        """Return all tasks that are not yet complete."""
        return [task for task in self.nodes.values() if not task.done]

    def visualize(self) -> None:
        """Print a simple dependency view of the task graph."""
        print("\n📊 Task Graph Dependencies:")
        for task_id in sorted(self.nodes.keys()):
            task = self.nodes[task_id]
            deps = getattr(task, "depends_on", [])
            status = "✅ done" if task.done else "⏳ pending"
            dep_list = ", ".join(str(dep) for dep in deps) if deps else "None"
            print(f"🧩 {task_id} | depends_on: {dep_list} | {status}")
