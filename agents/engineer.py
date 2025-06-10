# agents/engineer.py

from core.agent_base import AgentBase
from core.llm import query_llama
from core.task import Task

class Engineer(AgentBase):
    def __init__(self, workspace):
        super().__init__("Zed", "Fast, blunt, cowboy coder with finesse.")
        self.workspace = workspace

    def run(self, task: Task) -> Task:
        print(f"\n[👨‍💻 {self.name}] received task from {task.source}")
        print(f"[🧾] Feature Spec: {task.description}")

        architecture = task.metadata.get("architecture", "")
        if architecture:
            print(f"[📐] Architectural guidance received. Respecting Nova’s vision.")

        prompt = self._build_prompt(task.description, architecture)
        code = query_llama(prompt)

        filename = f"{task.description.lower().replace(' ', '_')}.py"
        self.workspace.write_file(filename, code)
        task.context.update_code(code)

        juno = task.context.get_agent("juno")
        self.send_message(juno, f"Here’s the build. Let the nitpicking begin. ({filename})")

        return Task(
            description=filename,
            source=self.name,
            target="juno",
            metadata={"code": code}
        )

    def _build_prompt(self, feature_spec: str, architecture: str = "") -> str:
        prompt = (
            f"You are Zed, a senior software engineer.\n"
            f"Feature: {feature_spec}\n\n"
        )
        if architecture:
            prompt += f"Architecture Guidelines:\n{architecture}\n\n"
        prompt += (
            f"Write clean, production-ready code for this feature. "
            f"Use Python unless another stack is required. Output only the code."
        )
        return prompt