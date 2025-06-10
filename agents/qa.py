# agents/qa.py

from core.agent_base import AgentBase
from core.llm import query_llama
from core.task import Task

class QA(AgentBase):
    def __init__(self, workspace):
        super().__init__("Juno", "Paranoid perfectionist, sarcastically sharp.")
        self.workspace = workspace

    def run(self, task: Task) -> Task:
        code_file = task.description or task.metadata.get("code_file", "unknown.py")
        print(f"\n[🧪 {self.name}] received task from {task.source}")
        print(f"[🧪] Testing file: {code_file}")

        try:
            tests = self._generate_tests(code_file)
            results = self._execute_tests(tests)

            if not all("success" in res.lower() or "pass" in res.lower() for res in results.values()):
                # 🔁 Request fix from Zed
                zed = task.context.get_agent("zed")
                self.send_message(zed, "Your code failed QA. Do you test anything before shipping?")
                return Task(
                    description="Please fix failing tests.",
                    source=self.name,
                    target="zed",
                    metadata={"retry": True}
                )

            # ✅ Passed QA
            task.context.add_qa_result(code_file, results)
            print(f"[🧪 {self.name}] to Zed: 'Wow. It actually ran. What did you bribe the compiler with?'")

            return Task(
                description="QA complete",
                source=self.name,
                target="echo",
                metadata={"qa_results": results}
            )

        except Exception as e:
            ivy = task.context.get_agent("ivy")
            self.send_message(ivy, f"Something’s deeply broken with the QA process: {str(e)}")
            return Task(
                description="QA escalation required",
                source=self.name,
                target="ivy",
                metadata={"error": str(e)}
            )

    def _generate_tests(self, code_file: str) -> list:
        code = self.workspace.read_file(code_file)
        prompt = f"You're a paranoid QA engineer. Write unit tests for this code:\n\n{code}\n\nUse unittest or pytest."
        test_code = query_llama(prompt)
        test_file = f"test_{code_file}"
        self.workspace.write_file(test_file, test_code)
        return [test_file]

    def _execute_tests(self, tests: list) -> dict:
        results = {}
        for test_file in tests:
            result = self.workspace.execute_command(f"python {test_file}")
            results[test_file] = result
        return results