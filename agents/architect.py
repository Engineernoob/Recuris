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
        return thread  # You may want to store/join this if needed

    def _process_task(self, task: Task):
        print(f"\n[👩🏽‍💻 {self.name}] received task from {task.source}")
        print(f"[🧠] Reviewing product spec...")

        architecture = self._design_arch(task.description)
        self.workspace.write_file("architecture.md", architecture)
        task.context.update_architecture(architecture)

        # 💬 Messaging Zed with a warning and handoff
        zed = task.context.get_agent("zed")
        self.send_message(zed, "Don’t mess up my clean architecture this time.")
        self.send_message(zed, f"Architecture doc is done. Check 'architecture.md'.")

        next_task = Task(
            description="Initial feature set based on architecture",
            source=self.name,
            target="zed",
            metadata={"architecture": architecture}
        )
        self.task_engine.add_task(next_task)  # if task_engine is available

    def _design_arch(self, spec: str) -> str:
        prompt = (
            f"You are Nova, a visionary software architect. "
            f"Based on this spec, recommend:\n"
            f"- Frontend framework\n- Backend tech\n- Database\n- API/tools\n"
            f"Then outline a clean modular architecture with file/folder structure.\n\n"
            f"Product Spec:\n{spec}"
        )
        return query_llama(prompt)