# agents/team_lead.py

from agents.planner import PlannerAgent

class TeamLead:
    def __init__(self, task_engine):
        self.name = "Ivy"
        self.personality = "Calm, strategic, delegation master"
        self.task_engine = task_engine
        self.planner = PlannerAgent()

    def run(self, user_request: str):
        print(f"[🧠 {self.name}] ({self.personality}) executing...")
        print(f"[🧭] Delegating to Orion for strategic breakdown...")

        # Orion plans everything
        tasks = self.planner.run(user_request)

        if not tasks:
            print(f"[🧠 {self.name}] Hmm. Orion seems stumped.")
            return []

        print(f"[🧠 {self.name}] Orion mapped {len(tasks)} tasks. Delegating to agents...")

        for task in tasks:
            print(f"[📌 Task] → {task.target}: {task.description}")
            self.task_engine.add_task(task)

        print(f"[🧠 {self.name}] ‘All agents briefed. Let’s build something brilliant.’")
        return tasks