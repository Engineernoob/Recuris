class Architect:
    def __init__(self, workspace):
        self.name = "Nova"
        self.personality = "Visionary, obsessed with clean architecture."
        self.workspace = workspace

    def run(self, spec: str):
        print(f"[👩🏽‍💻 {self.name}] ({self.personality}) designing architecture for: {spec}")
        architecture = self._design_arch(spec)
        print(f"[🔧 Agent] {self.__class__.__name__} executing...")
        print(f"[📝] Writing architecture to workspace...")
        self.workspace.write_file('architecture.md', architecture)
        return architecture

    def _design_arch(self, spec: str) -> str:
        return f"# Architecture Plan\nBased on spec: {spec}\n"