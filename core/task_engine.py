from agents.architect import Architect
from agents.engineer import Engineer
from agents.memory_agent import MemoryAgent
from agents.planner import PlannerAgent
from agents.product_manager import ProductManager
from agents.qa import QA
from agents.team_lead import TeamLead
from core.project_context import ProjectContext
from core.task import Task
from core.workspace import Workspace


# Optional: banter map
BANTER = {
    ("max", "nova"): "Let’s see if you can architect without overcomplicating it this time.",
    ("nova", "zed"): "Zed, try not to hardcode your way into hell again.",
    ("zed", "juno"): "Juno, I'm sending this with love and bugs. Probably.",
    ("juno", "zed"): "Your love has too many runtime errors.",
    ("zed", "max"): "Max, I'm sending this with love and bugs. Probably."
}

class TaskEngine:
    def __init__(self):
        self.workspace = Workspace()
        self.task_queue = []
        self.planner = PlannerAgent()
        self.context = None # Set up Later

        self.agents = {
            "ivy": TeamLead(self),
            "max": ProductManager(self),
            "nova": Architect(self.workspace, self),
            "zed": Engineer(self.workspace, self),
            "juno": QA(self.workspace, self),
            "echo": MemoryAgent()
        }

    def add_task(self, task: Task):
        self.task_queue.append(task)

    def route_task(self, task: Task):
        agent = self.agents.get(task.target)
        if not agent:
            print(f"⚠️ No agent found for: {task.target}")
            return

        print(f"\n📨 Routing task: {task.description}")
        print(f"👤 [{agent.name}] ({agent.personality}) receiving task from {task.source}")

        banter = BANTER.get((task.source, task.target))
        if banter:
            print(f"💬 [{agent.name}] to {task.source}: \"{banter}\"")

        try:
            result = agent.run(task)

            if not self._validate_output(result):
                raise ValueError("Agent returned no valid result.")

            if isinstance(result, Task):
                self.add_task(result)

        except Exception as e:
            print(f"❌ Task failed: {e}")
            print(f"🔁 [Orion] Replanning task: {task.description}")
            replans = self.planner.run(task.description)
            for replanned_task in replans:
                self.add_task(replanned_task)

    def execute_all(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            # Attach context before routing
            task.context = self.context
            self.route_task(task)

    def _validate_output(self, output):
        # Basic heuristic: result must be non-empty
        return output is not None and str(output).strip() != ""