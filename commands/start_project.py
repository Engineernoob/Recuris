import typer
import json
from datetime import datetime
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
    typer.secho(f"📦 Starting project: {request}", fg=typer.colors.BRIGHT_YELLOW)

    # Shared state
    workspace = Workspace()
    memory = MemoryAgent()

    # === TEAM LEAD ===
    typer.secho("\n🔧 Team Lead analyzing request...", fg=typer.colors.BLUE)
    lead = TeamLead(task_engine=None)
    tasks = lead._break_down_task(request)

    # === PRODUCT MANAGER ===
    typer.secho("\n📋 PRODUCT SPEC:", fg=typer.colors.CYAN)
    pm = ProductManager(None)
    spec = pm._draft_spec(tasks[0])
    typer.echo(spec)

    # === ARCHITECT ===
    typer.secho("\n🏗️ ARCHITECTURE PLAN:", fg=typer.colors.GREEN)
    architect = Architect(workspace)
    arch = architect.run(spec)
    typer.echo(arch)

    # === ENGINEER ===
    typer.secho("\n👨‍💻 ENGINEER OUTPUT:", fg=typer.colors.MAGENTA)
    engineer = Engineer(workspace)
    filename = engineer.run("Initial feature set")
    typer.echo(f"Code written to: {filename}")

    # === QA ===
    typer.secho("\n✅ QA RESULTS:", fg=typer.colors.BRIGHT_GREEN)
    qa = QA(workspace)
    test_results = qa.run(filename)
    typer.echo(str(test_results))

    # === MEMORY ===
    memory.store({
        "id": request,
        "spec": spec,
        "architecture": arch,
        "filename": filename,
        "qa_results": test_results
    })
    typer.secho("\n📁 Project state saved to memory.", fg=typer.colors.YELLOW)

    # === README.md ===
    readme_content = f"""# Recuris AI Project

## 🧠 User Request
{request}

## 📋 Product Spec
{spec}

## 🏗️ Architecture Plan
{arch}

## 👨‍💻 Output
Code written to `{filename}`

## ✅ QA Results
{test_results}
"""
    workspace.write_file("README.md", readme_content)
    typer.secho("📄 README.md generated.", fg=typer.colors.CYAN)

    # === OUTPUT LOG ===
    output_path = f"data/output/session_{datetime.now().isoformat()}.json"
    with open(output_path, 'w') as f:
        json.dump({
            "request": request,
            "spec": spec,
            "architecture": arch,
            "filename": filename,
            "qa_results": test_results
        }, f, indent=2)
    typer.secho(f"🧾 Output log saved to: {output_path}", fg=typer.colors.BRIGHT_WHITE)

if __name__ == "__main__":
    app()