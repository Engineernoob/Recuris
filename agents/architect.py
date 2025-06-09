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
        return f"# Architecture Plan\nBased on spec: {spec}\n"