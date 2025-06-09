# recuris.py
import typer
from commands.start_project import build_project

app = typer.Typer(help="🧠 Recuris – Your Autonomous AI Software Team")

@app.command()
def build():
    typer.secho("🤖 Recuris: What would you like to build today?", fg=typer.colors.BRIGHT_CYAN)
    request = typer.prompt("🧠 Your Idea")

    typer.secho("\n🧱 Should I pick the framework for this project?", fg=typer.colors.GREEN)
    framework_pref = typer.prompt("💬 Type 'auto' or name your preferred stack (e.g. Next.js + Supabase)")

    typer.secho("\n⚙️ Any additional preferences? (APIs, DBs, integrations)", fg=typer.colors.MAGENTA)
    extras = typer.prompt("🔧 Optional (press Enter to skip)")

    full_request = f"{request}. Preferred framework: {framework_pref}. Extras: {extras}"

    typer.secho("\n✅ Ready to begin!", fg=typer.colors.YELLOW)
    confirm = typer.confirm("Shall I start the autonomous build?")

    if confirm:
        build_project(full_request)
    else:
        typer.secho("❌ Build canceled. Come back anytime.", fg=typer.colors.RED)

if __name__ == "__main__":
    app()