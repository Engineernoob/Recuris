import json
import threading

from core.llm import query_llama
from core.task import Task
from core.task_graph import TaskGraph

class PlannerAgent:
    def __init__(self):
        self.name = "Orion"
        self.personality = "Hyper-logical strategist, sees the whole board."
        self.graph = TaskGraph()
        self.inbox = []
        self.task_results = []

    def visualize(self):
        for tid, deps in self.graph.edges.items():
            print(f"{tid} depends on {deps}")

    def run(self, goal: str, context=None, callback=None):
        def plan():
            print(f"\n[🧠 {self.name}] ({self.personality}) planning full task flow for:")
            print(f"📋 Goal: {goal}")

            context_local = context or {}
            framework = context_local.agent_notes.get("framework", "auto") if hasattr(context_local, "agent_notes") else "auto"

            prompt = (
                f"You are Orion, a brilliant AI project planner coordinating a dev team.\n"
                f"Goal: {goal}\n"
                f"Preferred Framework: {framework}\n\n"
                f"Break it into 4–6 sequential or parallel tasks as a JSON list with this format:\n"
                f'[{{"target": "zed", "description": "...", "depends_on": ["task_id"]}}]'
            )

            response = query_llama(prompt).strip()

            # ✅ Remove markdown fences and extra explanations
            if "```json" in response:
                response = response.split("```json")[-1].split("```")[0].strip()
            elif "```" in response:
                response = response.split("```")[-1].strip()

            try:
                parsed = json.loads(response)
                if not isinstance(parsed, list):
                    raise ValueError("Parsed LLM output is not a list of tasks.")
            except Exception as e:
                print(f"⚠️ Planner LLM error: {e}")
                print(f"📭 Raw response was: {repr(response)}")
                fallback = [Task(description=f"DEFINE_SPEC: {goal}", source=self.name, target="max")]
                if callback:
                    callback(fallback)
                self.task_results = fallback
                return

            task_objs = []
            for i, task in enumerate(parsed):
                t = Task(
                    id=f"task_{i}",
                    target=task.get("target", "zed"),
                    description=task.get("description", ""),
                    source=self.name,
                    depends_on=task.get("depends_on") or [],
                    metadata={"goal": goal}
                )
                self.graph.add_task(t)
                task_objs.append(t)

            self.task_results = task_objs
            if callback:
                callback(task_objs)

        thread = threading.Thread(target=plan)
        thread.start()
        return thread  # Optional: return thread if caller wants to track or join