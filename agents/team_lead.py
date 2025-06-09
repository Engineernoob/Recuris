# agents/team_lead.py
from core.task import Task

class TeamLead:
    def __init__(self, task_engine):
        self.name = "Ivy"
        self.personality = "Calm, strategic, delegation master"
        self.task_engine = task_engine

    def run(self, task: Task) -> Task:
        print(f"\n[🧠 {self.name}] ({self.personality}) received task from {task.source}")
        print(f"[📝] Analyzing and delegating...")

        tasks = self._break_down_task(task.description)

        # Only forwarding to Max for now; others will be routed automatically later
        print(f"[🧠 {self.name}] to Max: 'Set the direction clearly. I trust you.'")
        return Task(
            description=tasks[0],
            source="ivy",
            target="max"
        )

    def _break_down_task(self, request: str) -> list:
        return [
            f"DEFINE_SPEC: {request}",
            f"ARCHITECTURE_PLAN: {request}",
            f"IMPLEMENT_FEATURES: {request}"
        ]