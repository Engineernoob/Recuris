# agents/product_manager.py

import threading
from core.agent_base import AgentBase
from core.llm import query_llama
from core.task import Task

class ProductManager(AgentBase):
    def __init__(self, task_engine):
        super().__init__("Max", "Analytical, detail-obsessed, UX-focused.")
        self.task_engine = task_engine

    def run(self, task: Task):
        thread = threading.Thread(target=self._process_task, args=(task,))
        thread.start()
        return thread  # Optional: return thread if you want to manage it

    def _process_task(self, task: Task):
        print(f"\n[📋 {self.name}] received task from {task.source}")
        print(f"[📝] Drafting product spec for: {task.description}")

        spec = self._draft_spec(task.description)
        task.context.update_spec(spec)

        nova = self.task_engine.agents.get("nova")
        self.send_message(nova, "Let’s see if you can architect this without overcomplicating it again.")
        self.send_message(nova, f"Here’s the finalized spec: {spec}")

        next_task = Task(
            description=spec,
            source=self.name,
            target="nova",
            metadata={"spec": spec}
        )
        self.task_engine.add_task(next_task)

    def _draft_spec(self, task: str) -> str:
        prompt = f"You're a product manager. Write a clear spec for: {task}"
        return query_llama(prompt)