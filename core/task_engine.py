from agents.architect import Architect
from agents.engineer import Engineer
from agents.memory_agent import MemoryAgent
from agents.product_manager import ProductManager
from agents.qa import QA
from agents.team_lead import TeamLead
from core.project_context import ProjectContext
from core.task import Task
from core.workspace import Workspace

BANTER = {
    ("max", "nova"): "Let’s see if you can architect without overcomplicating it this time.",
    ("nova", "zed"): "Zed, try not to hardcode your way into hell again.",
    ("zed", "juno"): "Juno, I'm sending this with love and bugs. Probably.",
    ("juno", "zed"): "Your love has too many runtime errors.",
    ("zed", "max"): "Max, I'm sending this with love and bugs. Probably.",
}


class TaskEngine:
    def __init__(self, context: ProjectContext | None = None):
        self.workspace = Workspace()
        self.task_queue: list[Task] = []
        self.context = context

        self.agents = {
            "ivy": TeamLead(self),
            "max": ProductManager(self),
            "nova": Architect(self.workspace, self),
            "zed": Engineer(self.workspace, self),
            "juno": QA(self.workspace, self),
            "echo": MemoryAgent(),
        }

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            print(f"⚠️ Tried to queue a non-Task object: {type(task).__name__}")
            return
        self.task_queue.append(task)

    def get_agent(self, agent_key: str):
        agent = self.agents.get(agent_key)
        if not agent:
            available = ", ".join(sorted(self.agents.keys()))
            raise KeyError(f"Unknown agent '{agent_key}'. Available agents: {available}")
        return agent

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

            if result is None:
                return

            if not self._validate_output(result):
                print(f"⚠️ Invalid output from {agent.name} for task: {task.description}")
                return

            if isinstance(result, Task):
                self.add_task(result)
            elif isinstance(result, list):
                for item in result:
                    if isinstance(item, Task):
                        self.add_task(item)
                    else:
                        print(
                            f"⚠️ Skipping non-Task item returned by {agent.name}: {type(item).__name__}"
                        )

        except Exception as e:
            print(f"❌ Task failed: {e}")
            print(f"🔁 [Orion] Replanning task: {task.description}")

            from agents.planner import PlannerAgent

            planner = PlannerAgent()

            def handle_replans(tasks):
                if not tasks:
                    print("⚠️ Failed to replan task.")
                    return
                for replanned_task in tasks:
                    self.add_task(replanned_task)

            planner.run(task.description, context=self.context, callback=handle_replans)

    def execute_all(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            task.context = self.context
            self.route_task(task)

    def _validate_output(self, output):
        if output is None:
            return False
        if isinstance(output, list):
            return len(output) > 0
        return str(output).strip() != ""