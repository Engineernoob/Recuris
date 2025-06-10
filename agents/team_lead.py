# agents/team_lead.py

from core.agent_base import AgentBase
from agents.planner import PlannerAgent
from core.task import Task

class TeamLead(AgentBase):
    def __init__(self, task_engine):
        super().__init__("Ivy", "Calm, strategic, delegation master")
        self.task_engine = task_engine
        self.planner = PlannerAgent()

    def run(self, user_request: str):
        print(f"\n[🧠 {self.name}] executing request from user...")
        print(f"[🧭] Orion, I need a project plan for: {user_request}")

        tasks = self.planner.run(user_request)

        if not tasks:
            print(f"[🧠 {self.name}] Orion seems stumped. Falling back to default structure.")
            tasks = self._fallback_tasks(user_request)

        self.send_message(self.planner.name, f"Got {len(tasks)} tasks. Starting handoff.")

        for task in tasks:
            print(f"[📌 Task] → {task.target}: {task.description}")
            self.task_engine.add_task(task)

        print(f"[🧠 {self.name}] ‘All agents briefed. Let’s build something brilliant.’")
        return tasks

    def _fallback_tasks(self, request: str) -> list:
        return [
            Task(description=f"DEFINE_SPEC: {request}", source=self.name, target="max"),
            Task(description=f"ARCHITECTURE_PLAN: {request}", source=self.name, target="nova"),
            Task(description=f"IMPLEMENT_FEATURES: {request}", source=self.name, target="zed")
        ]