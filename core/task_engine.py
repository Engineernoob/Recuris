from agents.team_lead import TeamLead
from agents.product_manager import ProductManager
from agents.architect import Architect
from agents.engineer import Engineer
from agents.qa import QA
from core.workspace import Workspace
from core.task import Task

# Optional: banter map
BANTER = {
    ("max", "nova"): "Let’s see if you can architect without overcomplicating it this time.",
    ("nova", "zed"): "Zed, try not to hardcode your way into hell again.",
    ("zed", "juno"): "Juno, I'm sending this with love and bugs. Probably.",
    ("juno", "zed"): "Your love has too many runtime errors.",
}

class TaskEngine:
    def __init__(self):
        self.workspace = Workspace()

        self.agents = {
            "ivy": TeamLead(self),
            "max": ProductManager(self),
            "nova": Architect(self.workspace),
            "zed": Engineer(self.workspace),
            "juno": QA(self.workspace)
        }

    def route_task(self, task: Task):
        current_agent = self.agents.get(task.target)

        if not current_agent:
            print(f"⚠️ No agent found for: {task.target}")
            return

        print(f"\n📨 Routing task: {task.description}")
        print(f"👤 [{current_agent.name}] ({current_agent.personality}) receiving task from {task.source}")

        # Optional banter
        banter = BANTER.get((task.source, task.target))
        if banter:
            print(f"💬 [{current_agent.name}] to {task.source}: \"{banter}\"")

        # Run the task
        result = current_agent.run(task)

        # If another task is returned, route it too
        if isinstance(result, Task):
            self.route_task(result)