class Architect:
    def __init__(self, workspace):
        self.workspace = workspace

    def run(self, spec: str):
        architecture = self._design_arch(spec)
        self.workspace.write_file('architecture.md', architecture)
        return architecture

    def _design_arch(self, spec: str) -> str:
        return f"# Architecture Plan\nBased on spec: {spec}\n"