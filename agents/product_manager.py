from core.llm import query_llama
from core.task import Task

class ProductManager:
    def __init__(self, task_engine):
        self.name = "Max"
        self.personality = "Analytical, detail-obsessed, UX-focused."
        self.task_engine = task_engine

    def run(self, task: Task) -> Task:
        print(f"\n[📋 {self.name}] ({self.personality}) received task from {task.source}")
        print(f"[📝] Drafting spec for: {task.description}")

        spec = self._draft_spec(task.description)
        print(f"[📋 {self.name}] → Spec ready. Sending to Nova...")
        task.context.update_spec(spec)

        # Optional friendly jab
        print(f"[📋 {self.name}] to Nova: 'Let’s see if you can architect this without overcomplicating it again.'")

        return Task(
            description=spec,
            source="max",
            target="nova"
        )

    def _draft_spec(self, task: str) -> str:
        prompt = f"You're a product manager. Write a clear spec for: {task}"
        return query_llama(prompt)