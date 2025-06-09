from core.task import Task

class Engineer:
    def __init__(self, workspace):
        self.name = "Zed"
        self.personality = "Fast, blunt, cowboy coder with finesse."
        self.workspace = workspace

    def run(self, task: Task) -> Task:
        print(f"\n[👨‍💻 {self.name}] ({self.personality}) received task from {task.source}")
        print(f"[🧾] Feature Spec: {task.description}")

        print(f"[🔧] Writing code to workspace...")
        code = self._generate_code(task.description)

        filename = f"{task.description.lower().replace(' ', '_')}.py"
        self.workspace.write_file(filename, code)

        print(f"[👨‍💻 {self.name}] to Juno: 'I’m sure you’ll find something to nitpick.'")

        return Task(
            description=filename,
            source="zed",
            target="juno",
            metadata={"code": code}
        )

    def _generate_code(self, spec: str) -> str:
        return f"# Code implementation for {spec}\n"