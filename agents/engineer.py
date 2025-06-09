class Engineer:
    def __init__(self, workspace):
        self.name = "Zed"
        self.personality = "Fast, blunt, cowboy coder with finesse."
        self.workspace = workspace

    def run(self, feature_spec: str) -> str:
        print(f"[👨‍💻 {self.name}] ({self.personality}) writing code for: {feature_spec}")
        print(f"[🔧 Agent] {self.__class__.__name__} executing...")
        print(f"[📝] Writing code to workspace...")
        code = self._generate_code(feature_spec)
        filename = f"{feature_spec.lower().replace(' ', '_')}.py"
        self.workspace.write_file(filename, code)
        return filename

    def _generate_code(self, spec: str) -> str:
        return f"# Code implementation for {spec}\n"