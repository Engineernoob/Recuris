# recuris.py

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

    ivy = engine.agents["ivy"]

    # ✅ Callback to start execution once Ivy finishes planning
    def on_plan_finished():
        typer.secho("\n🚀 Executing planned tasks...\n", fg=typer.colors.BRIGHT_GREEN)
        engine.execute_all()

    # ⏳ Begin planning + delegation with callback
    typer.secho("\n🚧 Planning in progress… agents will work in the background.\n", fg=typer.colors.BRIGHT_BLUE)
    ivy.run(request, done_callback=on_plan_finished)

if __name__ == "__main__":
    app()
# recuris.py

import typer
from typing_extensions import Annotated

from core.project_context import ProjectContext
from core.task_engine import TaskEngine

app = typer.Typer(help="🧠 Recuris – Your Autonomous AI Software Team")


@app.command()
def build(
    request: Annotated[
        str | None,
        typer.Argument(help="What you want Recuris to build.", show_default=False),
    ] = None,
    framework: Annotated[
        str | None,
        typer.Option(
            "--framework",
            "-f",
            help="Preferred framework or stack. Use 'auto' to let Recuris choose.",
        ),
    ] = None,
    extras: Annotated[
        str | None,
        typer.Option(
            "--extras",
            "-e",
            help="Optional APIs, databases, integrations, or constraints.",
        ),
    ] = None,
    yes: Annotated[
        bool,
        typer.Option(
            "--yes",
            "-y",
            help="Skip the confirmation prompt and start immediately.",
        ),
    ] = False,
):
    """Plan and execute an autonomous software build task."""

    typer.secho("🤖 Recuris: Autonomous build command", fg=typer.colors.BRIGHT_CYAN)

    if not request:
        request = typer.prompt("🧠 What would you like to build?")

    if framework is None:
        typer.secho(
            "\n🧱 Framework selection",
            fg=typer.colors.GREEN,
        )
        framework = typer.prompt(
            "💬 Type 'auto' or name your preferred stack",
            default="auto",
            show_default=True,
        )

    if extras is None:
        typer.secho(
            "\n⚙️ Additional preferences",
            fg=typer.colors.MAGENTA,
        )
        extras = typer.prompt(
            "🔧 APIs, DBs, integrations, or constraints",
            default="",
            show_default=False,
        )

    typer.secho("\n📋 Build summary", fg=typer.colors.YELLOW)
    typer.echo(f"Goal: {request}")
    typer.echo(f"Framework: {framework}")
    typer.echo(f"Extras: {extras or 'None'}")

    if not yes:
        confirm = typer.confirm("\n✅ Start the autonomous build?")
        if not confirm:
            typer.secho("❌ Build canceled. Come back anytime.", fg=typer.colors.RED)
            raise typer.Exit()

    context = ProjectContext(goal=request)
    context.agent_notes["framework"] = framework
    context.agent_notes["extras"] = extras or ""

    engine = TaskEngine()
    engine.context = context

    ivy = engine.agents["ivy"]

    def on_plan_finished():
        typer.secho("\n🚀 Plan complete. Executing tasks...\n", fg=typer.colors.BRIGHT_GREEN)
        engine.execute_all()
        typer.secho("\n🏁 Recuris finished executing the task queue.\n", fg=typer.colors.BRIGHT_YELLOW)

    typer.secho("\n🧭 Ivy is planning the build now...\n", fg=typer.colors.BRIGHT_BLUE)
    ivy.run(request, done_callback=on_plan_finished)


if __name__ == "__main__":
    app()