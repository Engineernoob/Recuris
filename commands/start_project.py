# commands/start_project.py
import typer
from agents.team_lead import TeamLead
from agents.product_manager import ProductManager
from agents.architect import Architect
from agents.engineer import Engineer
from agents.qa import QA
from agents.memory_agent import MemoryAgent
from core.workspace import Workspace

app = typer.Typer()

@app.command()
def start(request: str):
    """Start a new autonomous project build."""
    typer.echo(f"📦 Starting project: {request}")

    # Shared state
    workspace = Workspace()
    memory = MemoryAgent()

    # Simulated agent calls
    lead = TeamLead(task_engine=None)  # No dispatcher yet
    tasks = lead._break_down_task(request)

    # Run agent logic manually for now
    pm = ProductManager(None)
    spec = pm._draft_spec(tasks[0])
    typer.echo(f"📋 Product Spec:\n{spec}")

    architect = Architect(workspace)
    arch = architect.run(spec)
    typer.echo(f"🏗️ Architecture:\n{arch}")

    engineer = Engineer(workspace)
    filename = engineer.run("Initial feature set")
    typer.echo(f"👨‍💻 Code written to: {filename}")

    qa = QA(workspace)
    test_results = qa.run(filename)
    typer.echo(f"✅ QA Results: {test_results}")

    memory.store({"id": request, "spec": spec, "arch": arch, "filename": filename})
    typer.echo("📁 Project state saved to memory.")

if __name__ == "__main__":
    app()