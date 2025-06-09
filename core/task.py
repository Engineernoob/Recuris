class Task:
    def __init__(self, description: str, source: str, target: str, metadata=None):
        self.description = description
        self.source = source
        self.target = target
        self.metadata = metadata or {}

    def __repr__(self):
        return f"<Task {self.description} ({self.source} ➝ {self.target})>"