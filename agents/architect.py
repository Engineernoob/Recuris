# agents/architect.py

import threading
from core.agent_base import AgentBase
from core.llm import query_llama
from core.task import Task

class Architect(AgentBase):
    def __init__(self, workspace, task_engine):
        super().__init__("Nova", "Visionary, obsessed with clean architecture.")
        self.workspace = workspace
        self.task_engine = task_engine

    def run(self, task: Task):
        thread = threading.Thread(target=self._process_task, args=(task,))
        thread.start()
        return thread

    def _process_task(self, task: Task):
        print(f"\n[👩🏽‍💻 {self.name}] received task from {task.source}")
        print(f"[🧠] Reviewing product spec...")

        try:
            architecture = self._design_arch(task.description)
        except Exception as e:
            architecture = f"Error during architecture generation: {str(e)}"
            print(f"[⚠️ Nova] LLM error: {e}")

        try:
            self.workspace.write_file("architecture.md", architecture)
            task.context.update_architecture(architecture)
        except Exception as e:
            print(f"[⚠️ Nova] Failed to write or update architecture: {e}")

        zed = task.context.get_agent("zed")
        if zed:
            self.send_message(zed, "Don’t mess up my clean architecture this time.")
            self.send_message(zed, f"Architecture doc is done. Check 'architecture.md'.")
        else:
            print("[⚠️ Nova] Zed not found in context.")

        next_task = Task(
            description="Initial feature set based on architecture",
            source=self.name,
            target="zed",
            metadata={"architecture": architecture}
        )
        self.task_engine.add_task(next_task)

    def _design_arch(self, spec: str) -> str:
        prompt = (
            f"You are Nova, a visionary software architect.\n"
            f"Based on this product spec, recommend:\n"
            f"- Frontend framework\n- Backend tech\n- Database\n- APIs or integrations\n\n"
            f"Then provide a modular architecture with clean file/folder structure.\n\n"
            f"Spec:\n{spec}"
        )
        return query_llama(prompt)