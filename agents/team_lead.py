# agents/team_lead.py

import threading
from typing import Callable, Optional
from core.agent_base import AgentBase
from agents.planner import PlannerAgent
from core.task import Task

class TeamLead(AgentBase):
    def __init__(self, task_engine: object):
        super().__init__("Ivy", "Calm, strategic, delegation master")
        self.task_engine = task_engine
        self.planner = PlannerAgent()
        self._plan_complete_event = threading.Event()

    def run(self, user_request: str, done_callback: Optional[Callable[[], None]] = None):
        print(f"\n[🧠 {self.name}] executing request from user...")
        print(f"[🧭] Orion, I need a project plan for: {user_request}")
        print("[⏳] Planning in progress...")

        def handle_plan_result(tasks: list[Task]):
            if not tasks:
                print(f"[🧠 {self.name}] Orion seems stumped. Falling back to default structure.")
                tasks = self._fallback_tasks(user_request)

            self.send_message(self.planner, f"Got {len(tasks)} tasks. Starting handoff.")

            for task in tasks:
                print(f"[📌 Task] → {task.target}: {task.description}")
                self.task_engine.add_task(task)

            print(f"[🧠 {self.name}] ‘All agents briefed. Let’s build something brilliant.’")
            self._plan_complete_event.set()

            if done_callback:
                done_callback()  # ✅ Trigger the engine once planning is done

        self.planner.run(user_request, context=self.task_engine.context, callback=handle_plan_result)

    def _fallback_tasks(self, request: str) -> list[Task]:
        context = self.task_engine.context
        return [
            Task(description=f"DEFINE_SPEC: {request}", source=self.name, target="max", context=context),
            Task(description=f"ARCHITECTURE_PLAN: {request}", source=self.name, target="nova", context=context),
            Task(description=f"IMPLEMENT_FEATURES: {request}", source=self.name, target="zed", context=context)
        ]