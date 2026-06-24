import os
from pathlib import Path
from git import Repo, InvalidGitRepositoryError


class Workspace:
    """
    Handles file operations and Git tracking for generated artifacts.

    The workspace acts as the persistent environment where agents
    read and write files. All writes are automatically committed so
    agent outputs remain traceable.
    """

    def __init__(self, path: str = "."):
        self.path = Path(path).resolve()
        self.path.mkdir(parents=True, exist_ok=True)

        try:
            self.repo = Repo(self.path)
        except InvalidGitRepositoryError:
            self.repo = Repo.init(self.path)

    def _full_path(self, filepath: str) -> Path:
        """Resolve a workspace-relative file path."""
        return self.path / filepath

    def read_file(self, filepath: str) -> str:
        """Read a file from the workspace."""
        full_path = self._full_path(filepath)

        if not full_path.exists():
            return f"File not found: {filepath}"

        try:
            return full_path.read_text(encoding="utf-8")
        except Exception as e:
            return f"Error reading file {filepath}: {e}"

    def write_file(self, filepath: str, content: str, commit: bool = True):
        """
        Write a file to the workspace and optionally commit it.
        """
        full_path = self._full_path(filepath)
        full_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            full_path.write_text(content, encoding="utf-8")
        except Exception as e:
            raise RuntimeError(f"Failed to write {filepath}: {e}")

        if commit:
            rel_path = os.path.relpath(full_path, self.path)
            self.repo.git.add(rel_path)

            # Only commit if something actually changed
            if self.repo.is_dirty(untracked_files=True):
                self.repo.index.commit(f"Recuris: update {rel_path}")

    def push(self, remote: str = "origin", branch: str = "main"):
        """
        Push workspace commits to a remote repository.
        """
        try:
            self.repo.git.push(remote, branch)
        except Exception as e:
            raise RuntimeError(f"Push failed: {e}")