import yaml
from crewai import CrewAI

class TaskEngine:
    def __init__(self, config_path: str = 'core/crew.yaml'):
        config = yaml.safe_load(open(config_path))
        self.crew = CrewAI(config)

    def assign(self, task: str):
        self.crew.assign_task(task)

    def execute_all(self):
        self.crew.run_all()