# core/task_graph.py

class TaskGraph:
    def __init__(self):
        self.nodes = {}  # task_id (str) -> Task
        self.edges = {}  # task_id (str) -> list of dependent task_ids

    def add_task(self, task, task_id=None):
        # Safely extract ID
        task_id = task_id or task.metadata.get("task_id", task.description)
        self.nodes[task_id] = task
        self.edges.setdefault(task_id, [])

        # Ensure all depends_on values are strings
        for dep in getattr(task, "depends_on", []):
            if isinstance(dep, dict):
                print(f"⚠️ Skipping invalid dependency (dict): {dep}")
                continue
            if not isinstance(dep, str):
                dep = str(dep)
            self.edges.setdefault(dep, []).append(task_id)

    def mark_done(self, task_id):
        if task_id in self.nodes:
            self.nodes[task_id].done = True

    def get_ready_tasks(self):
        ready = []
        for task_id, task in self.nodes.items():
            if getattr(task, "done", False):
                continue
            deps = getattr(task, "depends_on", [])
            if all(self.nodes.get(d, None) and getattr(self.nodes[d], "done", False) for d in deps):
                ready.append(task)
        return ready

    def all_tasks(self):
        return list(self.nodes.values())

    def visualize(self):
        print("\n📊 Task Graph Dependencies:")
        for task_id, deps in self.edges.items():
            print(f"🧩 {task_id} depends on {deps}")