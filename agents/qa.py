from core.llm import query_llama
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
        task.context.add_qa_result(code_file, results)

        print(f"[🧪 {self.name}] to Zed: 'Wow. It actually ran. What did you bribe the compiler with?'")

        return Task(
            description="QA complete",
            source="juno",
            target="echo",
            metadata={"qa_results": results}
        )

    def _generate_tests(self, code_file: str) -> list:
        code = self.workspace.read_file(code_file)
        prompt = f"You're a paranoid software QA engineer. Write Python unit tests for the following code:\n\n{code}\n\n. Use the unittest or pytest style."
        test_code = query_llama(prompt)
        test_file = f"test_{code_file}"
        self.workspace.write_file(test_file, test_code)
        return [f"Generated {test_file}"]

    def _execute_tests(self, tests: list) -> dict:
        results = {}
        for test in tests:
            result = self.workspace.execute_command(f"python {test}")
            results[test] = result
        return results