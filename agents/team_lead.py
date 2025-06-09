# agents/team_lead.py
import json

from core.llm import query_llama
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
        prompt = (
        f"You are Ivy, a calm and strategic team lead. "
        f"Break down the following high-level product request into clear subtasks "
        f"for the following team members: Max (Product Spec), Nova (Architecture), Zed (Code), Juno (QA).\n\n"
        f"Request: {request}\n\n"
        f"Respond with a JSON array of objects like: "
        f'[{{"target": "max", "description": "..."}}]'
        )

        breakdown = query_llama(prompt)
        try:
            tasks = json.loads(breakdown)
            return [Task(**t, source="ivy") for t in tasks]
        except Exception:
            print("⚠️ Failed to parse LLM response — falling back to defaults.")
            return [
            Task(description=f"DEFINE_SPEC: {request}", source="ivy", target="max"),
            Task(description=f"ARCHITECTURE_PLAN: {request}", source="ivy", target="nova"),
            Task(description=f"IMPLEMENT_FEATURES: {request}", source="ivy", target="zed")
        ]