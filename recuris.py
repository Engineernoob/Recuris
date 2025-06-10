import typer

from core.project_context import ProjectContext
from core.task_engine import TaskEngine

app = typer.Typer(help="🧠 Recuris – Your Autonomous AI Software Team")

@app.command()
def build():
    typer.secho("🤖 Recuris: What would you like to build today?", fg=typer.colors.BRIGHT_CYAN)
    request = typer.prompt("🧠 Your Idea")

    typer.secho("\n🧱 Should I pick the framework for this project?", fg=typer.colors.GREEN)
    framework_pref = typer.prompt("💬 Type 'auto' or name your preferred stack (e.g. Next.js + Supabase)")

    typer.secho("\n⚙️ Any additional preferences? (APIs, DBs, integrations)", fg=typer.colors.MAGENTA)
    extras = typer.prompt("🔧 Optional (press Enter to skip)")

    typer.secho("\n✅ Ready to begin!", fg=typer.colors.YELLOW)
    confirm = typer.confirm("Shall I start the autonomous build?")

    if not confirm:
        typer.secho("❌ Build canceled. Come back anytime.", fg=typer.colors.RED)
        return

    # 🧠 Setup context
    context = ProjectContext(goal=request)
    context.agent_notes["framework"] = framework_pref
    context.agent_notes["extras"] = extras

    # 🛠️ Initialize engine + agents
    engine = TaskEngine()
    engine.context = context

    # 🧠 Start the process with Ivy
    ivy = engine.agents["ivy"]

    # ⏳ Begin planning + delegation
    typer.secho("\n🚧 Planning in progress… agents will work in the background.\n", fg=typer.colors.BRIGHT_BLUE)
    ivy.run(request)

if __name__ == "__main__":
    app()