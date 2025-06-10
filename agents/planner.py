# agents/planner.py
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
                f"Break the goal into 4–6 sequential or parallel tasks in JSON format. Each task must use one of the following agents as its 'target':\n"
                f"- max (Product Manager)\n- nova (Architect)\n- zed (Engineer)\n- juno (QA)\n- echo (Memory)\n\n"
                f"Use this format:\n"
                f"[{{\"target\": \"zed\", \"description\": \"...\", \"depends_on\": [\"task_0\"]}}]"
            )

            response = query_llama(prompt).strip()
            if "```json" in response:
                response = response.split("```json")[-1].split("```")[-2].strip()
            elif "```" in response:
                response = response.split("```")[-1].strip()

            try:
                parsed = json.loads(response)
                if not isinstance(parsed, list):
                    raise ValueError("Parsed response is not a list of tasks.")
            except Exception as e:
                print(f"⚠️ Planner LLM error: {e}")
                print(f"📭 Raw response was: {repr(response)}")
                fallback = [Task(description=f"DEFINE_SPEC: {goal}", source=self.name, target="max")]
                if callback:
                    callback(fallback)
                return

            task_objs = []
            for i, task in enumerate(parsed):
                task_id = f"task_{i}"
                raw_deps = task.get("depends_on", [])

                # 🛡️ Ensure dependencies are string IDs
                depends_on = []
                for dep in raw_deps:
                    if isinstance(dep, dict) and "id" in dep:
                        depends_on.append(dep["id"])
                    elif isinstance(dep, str):
                        depends_on.append(dep)

                t = Task(
                    target=task.get("target", "zed"),
                    description=task.get("description", ""),
                    source=self.name,
                    depends_on=depends_on,
                    metadata={"goal": goal, "task_id": task_id}
                )
                self.graph.add_task(t, task_id=task_id)
                task_objs.append(t)

            if callback:
                callback(task_objs)

        thread = threading.Thread(target=plan)
        thread.start()