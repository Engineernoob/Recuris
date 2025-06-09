# core/project_context.py
class ProjectContext:
    def __init__(self, goal: str):
        self.goal = goal
        self.spec = None
        self.architecture = None
        self.filenames = []
        self.qa_results = {}
        self.agent_notes = {}  # optional: {agent_name: note}

    def update_spec(self, spec: str):
        self.spec = spec

    def update_architecture(self, arch: str):
        self.architecture = arch

    def add_file(self, filename: str):
        self.filenames.append(filename)

    def add_qa_result(self, file: str, result: dict):
        self.qa_results[file] = result

    def add_note(self, agent: str, note: str):
        self.agent_notes[agent] = note