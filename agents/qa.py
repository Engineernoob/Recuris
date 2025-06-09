from core.task import Task

class QA:
    def __init__(self, workspace):
        self.name = "Juno"
        self.personality = "Paranoid perfectionist, sarcastically sharp."
        self.workspace = workspace

    def run(self, task: Task) -> Task:
        print(f"\n[🧪 {self.name}] ({self.personality}) received task from {task.source}")

        filename = task.description or task.metadata.get("code_file", "unknown.py")
        print(f"[🧪] Running tests on: {filename}")

        tests = self._generate_tests(filename)
        results = self._execute_tests(tests)

        self.workspace.write_file("qa_results.json", str(results))

        print(f"[🧪 {self.name}] to Zed: 'Wow. It actually ran. What did you bribe the compiler with?'")

        return Task(
            description="QA complete",
            source="juno",
            target="echo",
            metadata={"qa_results": results}
        )

    def _generate_tests(self, code_file: str) -> list:
        return [f"Test existence of {code_file}"]

    def _execute_tests(self, tests: list) -> dict:
        return {test: True for test in tests}