import typer
from core.task_engine import TaskEngine
from core.task import Task

app = typer.Typer()

@app.command()
def start(request: str):
    """Start a fully autonomous AI software build."""
    typer.secho("🧑‍💻 Meet the Recuris Dev Team:", fg=typer.colors.BRIGHT_MAGENTA)
    team = {
        "Ivy": "Calm, strategic, delegation master",
        "Max": "Analytical, detail-obsessed, UX-focused",
        "Nova": "Visionary, obsessed with clean architecture",
        "Zed": "Fast, blunt, cowboy coder with finesse",
        "Juno": "Paranoid perfectionist, sarcastically sharp",
        "Echo": "Ghost-like observer, remembers everything"
    }

    for name, trait in team.items():
        typer.echo(f" - {name}: {trait}")

    typer.secho(f"\n📦 Starting autonomous build: {request}", fg=typer.colors.YELLOW)

    # Initialize agent orchestration engine
    engine = TaskEngine()

    # Kick off the first task to Ivy (Team Lead)
    initial_task = Task(
        description=request,
        source="user",
        target="ivy"
    )

    engine.route_task(initial_task)

if __name__ == "__main__":
    app()