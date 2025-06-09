# recuris.py
import typer
from commands import start_project

app = typer.Typer(help="🧠 Recuris – Your Autonomous AI Software Team")

# Register the start command
app.command("start")(start_project.start)

if __name__ == "__main__":
    app()