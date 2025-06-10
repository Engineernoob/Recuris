import threading
from core.agent_base import AgentBase
from core.llm import query_llama
from core.task import Task
from core.task_engine import TaskEngine

class Engineer(AgentBase):
    def __init__(self, workspace):
        super().__init__("Zed", "Fast, blunt, cowboy coder with finesse.")
        self.workspace = workspace
        self.task_engine = TaskEngine()

    def run(self, task: Task):
        def build_code():
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

            next_task = Task(
                description=filename,
                source=self.name,
                target="juno",
                metadata={"code": code}
            )
            self.task_engine.add_task(next_task)

        threading.Thread(target=build_code).start()