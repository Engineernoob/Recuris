import os
from git import Repo

class Workspace:
    def __init__(self, path: str = '.'):
        self.path = path
        if not os.path.exists(os.path.join(path, '.git')):
            Repo.init(path)
        self.repo = Repo(path)

    def read_file(self, filepath: str) -> str:
        full_path = os.path.join(self.path, filepath)
        if not os.path.exists(full_path):
            return "No such file or directory"
        with open(full_path, 'r') as f:
            return f.read()

    def write_file(self, filepath: str, content: str):
        full_path = os.path.join(self.path, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
        self.repo.git.add(filepath)
        self.repo.index.commit(f"Add/update {filepath}")

    def push(self, remote: str = 'origin', branch: str = 'main'):
        self.repo.git.push(remote, branch)