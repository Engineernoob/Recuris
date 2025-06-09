# agents/team_lead.py
class TeamLead:
    def __init__(self, task_engine):
        self.task_engine = task_engine

    def run(self, user_request: str):
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