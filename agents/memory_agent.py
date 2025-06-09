import json
import os

from core.llm import query_llama
from core.task import Task

class MemoryAgent:
    def __init__(self, memory_dir: str = 'data/memory'):
        self.name = "Echo"
        self.personality = "Ghost-like observer, remembers everything."
        os.makedirs(memory_dir, exist_ok=True)
        self.memory_dir = memory_dir

    def run(self, task: Task) -> None:
        print(f"\n[👻 {self.name}] ({self.personality}) received task from {task.source}")
        print(f"[🧠] Archiving project summary...")

        entry = {
            "origin": task.source,
            "description": task.description,
            "metadata": task.metadata
        }

        # Generate a summary via LLM
        prompt = (
            f"You are Echo, an AI memory archivist.\n"
            f"Summarize this software project in 3 bullet points:\n\n"
            f"Task Description:\n{task.description}\n\n"
            f"Metadata:\n{json.dumps(task.metadata, indent=2)}"
        )
        entry["summary"] = query_llama(prompt)

        # Save to memory
        key = entry.get('description', f"session_{len(os.listdir(self.memory_dir))}")
        filename = f"{key.replace(' ', '_')}.json"
        path = os.path.join(self.memory_dir, filename)

        with open(path, 'w') as f:
            json.dump(entry, f, indent=2)

        print(f"[👻 {self.name}] Memory stored. This conversation never happened...")

    def retrieve(self, key: str) -> dict:
        path = os.path.join(self.memory_dir, f"{key}.json")
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
        return {}

    def recall(self, keyword: str):
        print(f"\n🧠 [Echo] Scanning memory for: '{keyword}'...\n")
        for file in os.listdir(self.memory_dir):
            if not file.endswith(".json"):
                continue
            with open(os.path.join(self.memory_dir, file)) as f:
                data = json.load(f)
                if keyword.lower() in json.dumps(data).lower():
                    print(f"🔹 Memory: {file}")
                    print(f"📝 Summary:\n{data.get('summary', 'No summary available.')}\n")