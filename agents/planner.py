# agents/planner.py

import json

from core.llm import query_llama
from core.task import Task
from core.task_graph import TaskGraph

class PlannerAgent:
    def __init__(self):
        self.name = "Orion"
        self.personality = "Hyper-logical strategist, sees the whole board."
        self.graph = TaskGraph()
        self.inbox = []

    def visualize(self):
        for tid, deps in self.graph.edges.items():
            print(f"{tid} depends on {deps}")

    def run(self, goal: str, context: dict = None) -> list:
        print(f"\n[🧠 {self.name}] ({self.personality}) planning full task flow for:")
        print(f"📋 Goal: {goal}")

        context = context or {}
        prompt = (
            f"You are Orion, a brilliant AI project planner coordinating a dev team.\n"
            f"Goal: {goal}\n\n"
            f"Break it into 4–6 sequential or parallel tasks as a JSON list with this format:\n"
            f'[{{"target": "zed", "description": "...", "depends_on": ["task_id"]}}]'
        )

        try:
            response = query_llama(prompt)
            parsed = json.loads(response)
        except Exception as e:
            print(f"⚠️ Planner LLM error: {e}")
            return [
                Task(description=f"DEFINE_SPEC: {goal}", source=self.name, target="max")
            ]

        task_objs = []
        for task in parsed:
            t = Task(
                target=task.get("target", "zed"),
                description=task.get("description", ""),
                source=self.name,
                depends_on=task.get("depends_on", []),
                metadata={"goal": goal}
            )
            self.graph.add_task(t)
            task_objs.append(t)

        return task_objs