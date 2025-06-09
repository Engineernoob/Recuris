class Task:
    def __init__(self, description, source, target, depends_on=None, metadata=None, context=None):
        self.description = description
        self.source = source
        self.target = target
        self.depends_on = depends_on or []
        self.metadata = metadata or {}
        self.context = context
        self.done = False

    def __str__(self):
        return f"Task({self.description}, source={self.source}, target={self.target}, depends_on={self.depends_on}, metadata={self.metadata}, context={self.context})"