import threading
from core.agent_base import AgentBase
from core.llm import query_llama
from core.task import Task

class Engineer(AgentBase):
    def __init__(self, workspace, task_engine):
        super().__init__("Zed", "Fast, blunt, cowboy coder with finesse.")
        self.workspace = workspace
        self.task_engine = task_engine

    def run(self, task: Task):
        def build_code():
            print(f"\n[👨‍💻 {self.name}] received task from {task.source}")
            print(f"[🧾] Feature Spec: {task.description}")

            architecture = task.metadata.get("architecture", "")
            if architecture:
                print(f"[📐] Architectural guidance received. Respecting Nova’s vision.")

            prompt = self._build_prompt(task.description, architecture)
            try:
                code = query_llama(prompt)
            except Exception as e:
                print(f"[🔥 Zed] LLM query failed: {e}")
                return

            filename = f"{task.description.lower().replace(' ', '_')}.py"
            try:
                self.workspace.write_file(filename, code)
                task.context.update_code(code)
            except Exception as e:
                print(f"[⚠️ Zed] Failed to write file or update context: {e}")
                return

            juno = task.context.get_agent("juno")
            if juno:
                self.send_message(juno, f"Here’s the build. Let the nitpicking begin. ({filename})")

                next_task = Task(
                    description=filename,
                    source=self.name,
                    target="juno",
                    metadata={"code": code}
                )
                self.task_engine.add_task(next_task)
            else:
                print("[⚠️ Zed] No QA agent (Juno) found in context.")

        threading.Thread(target=build_code).start()

    def _build_prompt(self, feature_spec: str, architecture: str) -> str:
        prompt = (
            f"You are Zed, a senior software engineer.\n"
            f"Your task is to build the code for a feature.\n\n"
            f"Feature: {feature_spec}\n\n"
        )
        if architecture:
            prompt += f"Architectural guidance:\n{architecture}\n\n"
        prompt += "Write clean, production-ready code. Output only the code."
        return prompt