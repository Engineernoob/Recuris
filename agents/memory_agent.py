import os
import json

class MemoryAgent:
    def __init__(self, memory_dir: str = 'data/memory'):
        os.makedirs(memory_dir, exist_ok=True)
        self.memory_dir = memory_dir

    def store(self, entry: dict):
        key = entry.get('id', str(len(os.listdir(self.memory_dir))))
        path = os.path.join(self.memory_dir, f"{key}.json")
        with open(path, 'w') as f:
            json.dump(entry, f)

    def retrieve(self, key: str) -> dict:
        path = os.path.join(self.memory_dir, f"{key}.json")
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
        return {}