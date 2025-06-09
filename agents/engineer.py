from core.llm import query_llama
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
        prompt =(
            f"You are Zed, a fast and blunt senior software engineer."
            f"Write production-quality code for the following feature:\n\n{spec}\n\n"
            f"Always check your code for correctness and adherence to best practices like a senior engineer."
            f"Only output the code. Use Python unless another stack is specified."    
        )
        return query_llama(prompt)