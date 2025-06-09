# recuris.py
import typer
from commands.start_project import start

def main():
    typer.run(start)

if __name__ == "__main__":
    main()