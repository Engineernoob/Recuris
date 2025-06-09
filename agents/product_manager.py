class ProductManager:
    def __init__(self, task_engine):
        self.task_engine = task_engine

    def run(self, task: str):
        spec = self._draft_spec(task)
        self.task_engine.assign(f"ARCHITECTURE_PLAN: {spec}")
        return spec

    def _draft_spec(self, task: str) -> str:
        # Placeholder: draft simple spec
        return f"Specification for {task}"