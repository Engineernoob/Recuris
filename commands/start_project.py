# commands/start_project.py
import typer
from core.task_engine import TaskEngine
from agents.team_lead import TeamLead

app = typer.Typer()

@app.command()
def start(request: str):
    """Start a new autonomous project build."""
    engine = TaskEngine()
    lead = TeamLead(engine)
    tasks = lead.run(request)
    typer.echo(f"🚀 Created tasks:\n  - " + "\n  - ".join(tasks))
    engine.execute_all()

if __name__ == "__main__":
    app()