class ProductManager:
    def __init__(self, task_engine):
        self.name = "Max"
        self.personality = "Analytical, detail-obsessed, UX-focused."
        self.task_engine = task_engine

    def run(self, task: str):
        print(f"[👨🏻‍💼] {self.name}: {self.personality}")
        print(f"[🔧 Agent] {self.__class__.__name__} executing...")
        print(f"[📝] Drafting spec...")
        spec = self._draft_spec(task)
        self.task_engine.assign(f"ARCHITECTURE_PLAN: {spec}")
        return spec

    def _draft_spec(self, task: str) -> str:
        # Placeholder: draft simple spec
        return f"Specification for {task}"