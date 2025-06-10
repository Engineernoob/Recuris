# agents/product_manager.py

from core.agent_base import AgentBase
from core.llm import query_llama
from core.task import Task

class ProductManager(AgentBase):
    def __init__(self, task_engine):
        super().__init__("Max", "Analytical, detail-obsessed, UX-focused.")
        self.task_engine = task_engine

    def run(self, task: Task) -> Task:
        print(f"\n[📋 {self.name}] received task from {task.source}")
        print(f"[📝] Drafting product spec for: {task.description}")

        spec = self._draft_spec(task.description)
        task.context.update_spec(spec)

        nova = self.task_engine.agents.get("nova")
        self.send_message(nova, "Let’s see if you can architect this without overcomplicating it again.")
        self.send_message(nova, f"Here’s the finalized spec: {spec}")

        return Task(
            description=spec,
            source=self.name,
            target="nova",
            metadata={"spec": spec}
        )

    def _draft_spec(self, task: str) -> str:
        prompt = f"You're a product manager. Write a clear spec for: {task}"
        return query_llama(prompt)