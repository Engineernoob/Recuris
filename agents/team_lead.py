# agents/team_lead.py
class TeamLead:
    def __init__(self, task_engine):
        self.name = "Ivy"
        self.personality = "Calm, strategic, delegation master"
        self.task_engine = task_engine

    def run(self, user_request: str):
        print(f"[🧠 {self.name}] ({self.personality}) executing...")
        print(f"[👨‍💼 Agent] {self.__class__.__name__} executing...")
        print(f"[📝] Decomposing task...")
        """
        Decompose a high-level request into tasks and assign them.
        """
        tasks = self._break_down_task(user_request)
        for task in tasks:
            self.task_engine.assign(task)
        return tasks

    def _break_down_task(self, request: str):
        # Placeholder logic: split on sentences or keywords
        return [f"DEFINE_SPEC: {request}", f"ARCHITECTURE_PLAN: {request}", f"IMPLEMENT_FEATURES: {request}"]