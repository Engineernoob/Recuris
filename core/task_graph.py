# core/task_graph.py

class TaskGraph:
    def __init__(self):
        self.nodes = {}  # task_id (str) -> Task
        self.edges = {}  # task_id (str) -> list of dependent task_ids

    def add_task(self, task, task_id=None):
        task_id = task_id or task.description
        self.nodes[task_id] = task
        self.edges.setdefault(task_id, [])

        for dep in getattr(task, "depends_on", []):
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
            if all(self.nodes[d].done for d in deps if d in self.nodes):
                ready.append(task)
        return ready

    def all_tasks(self):
        return list(self.nodes.values())