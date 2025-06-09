from core.llm import query_llama
from core.task import Task

class Architect:
    def __init__(self, workspace):
        self.name = "Nova"
        self.personality = "Visionary, obsessed with clean architecture."
        self.workspace = workspace

    def run(self, task: Task) -> Task:
        print(f"\n[👩🏽‍💻 {self.name}] ({self.personality}) received task from {task.source}")
        print(f"[🧠] Reviewing spec: {task.description}")

        architecture = self._design_arch(task.description)
        print(f"[📝] Writing architecture to workspace...")
        self.workspace.write_file("architecture.md", architecture)

        print(f"[👩🏽‍💻 {self.name}] to Zed: 'Don’t mess up my clean architecture this time.'")

        return Task(
            description="Initial feature set based on architecture",
            source="nova",
            target="zed",
            metadata={"architecture": architecture}
        )

    def _design_arch(self, spec: str) -> str:
        prompt = (
        f"You are Nova, a visionary software architect. "
        f"Given the following product spec, suggest the best tech stack "
        f"and outline the architecture in markdown format.\n\n"
        f"Product Spec:\n{spec}\n\n"
        f"List:\n- Recommended frontend\n- Backend\n- Database\n- Any APIs or tools\n\n"
        f"Follow this with a detailed module breakdown and folder structure."
        )
        return query_llama(prompt)