# Recuris

Recuris is a multi-agent software development system designed to break down, execute, and review programming tasks through collaboration between specialized AI agents.

Instead of relying on a single general-purpose assistant, Recuris organizes work across dedicated roles such as architecture, engineering, and quality assurance, allowing complex software tasks to be handled in a more structured and iterative way.

## Why Recuris?

Recuris explores a more realistic model of AI-assisted software development:

- **Specialized agents** handle distinct responsibilities
- **Task decomposition** breaks larger goals into manageable steps
- **Shared memory** preserves context between sessions
- **QA feedback loops** improve output quality before completion

This makes Recuris useful as both:

- an experiment in multi-agent orchestration
- a foundation for AI-powered software workflow automation

## Features

- Multi-agent collaboration for software tasks
- Role-based agents such as Architect, Engineer, and QA
- Task planning and execution pipeline
- Persistent memory between sessions
- Configurable LLM backends
- Structured workspace and messaging system

## Project Structure

```text
Recuris/
├── agents/          # Specialized agents (Architect, Engineer, QA, etc.)
├── core/            # Task manager, messaging, orchestration, workspace logic
├── data/            # Memory files, artifacts, and outputs from previous sessions
├── recuris.py       # Main entry point
├── crew.yaml        # Agent definitions and workflow configuration
└── llm_config.yaml  # LLM provider and model settings
```

## How It Works

    1.Define agents in crew.yaml
    2.Configure models in llm_config.yaml
    3.Start Recuris with the main entry point
    4.Agents collaborate to:
    - interpret the task
    - plan the work
    - execute implementation steps
    - review results for quality

## Getting Started

Prerequisites

- Python 3.8+
- pip

## Installation

```bash
git clone <your-repo-url>
cd Recuris
pip install -r requirements.txt
```

## Configuration

Update the following files before running:

- crew.yaml for agent roles and workflow behavior
- llm_config.yaml for model/provider settings

## Run

```bash
python recuris.py
```

## Example Use Cases

- Generate small application scaffolds
- Break down feature requests into implementation tasks
- Run agent-based review and QA workflows
-     Experiment with autonomous development pipelines

## Documentation

- architecture.md for system design and architecture details
- Agent-specific documentation inside agents/

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
