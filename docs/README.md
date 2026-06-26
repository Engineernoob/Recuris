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

```
User Task
↓
Command / Task Routing
↓
Architect Agent
↓
Engineer Agent
↓
QA Agent
↓
Saved Artifacts + Memory
```

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

# Recuris

> An AI-native, multi-agent software engineering platform that coordinates specialized autonomous agents to plan, build, test, document, and maintain software projects.

Recuris explores a modular approach to AI-assisted software development by assigning well-defined responsibilities to independent agents instead of relying on a single general-purpose model. The result is a more structured, collaborative, and extensible engineering workflow.

---

## Why Recuris?

Traditional AI coding assistants are excellent at solving isolated tasks but often struggle to maintain context across larger software projects.

Recuris addresses this by introducing:

- 🤖 Specialized AI agents with clearly defined responsibilities
- 📋 Task decomposition for complex engineering work
- 🧠 Shared memory across agents
- 🔄 Feedback loops that improve solution quality
- 📚 Persistent project knowledge for long-running development

Recuris serves both as an experimental multi-agent framework and as a foundation for autonomous software engineering workflows.

---

## Features

- Multi-agent software development
- Autonomous task planning
- Agent-to-agent collaboration
- Shared semantic memory
- Configurable LLM providers
- Workspace management
- Persistent project artifacts
- Extensible orchestration engine

---

## Architecture Overview

```text
                 User
                  │
                  ▼
          CLI / Web Dashboard
                  │
                  ▼
        Orchestration Engine
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Architect    Engineer      QA Agent
     │            │            │
     └────────────┼────────────┘
                  ▼
          Shared Knowledge Layer
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
 PostgreSQL   Vector DB   Artifacts
```

---

## Project Structure

```text
Recuris/
├── agents/            # Specialized autonomous agents
├── core/              # Orchestration engine
├── data/              # Persistent memory and artifacts
├── docs/              # Project documentation
├── recuris.py         # Application entry point
├── crew.yaml          # Agent configuration
├── llm_config.yaml    # Model configuration
└── requirements.txt
```

---

## Workflow

1. User submits a software engineering task.
2. The orchestration engine decomposes the work.
3. Specialized agents collaborate on planning, implementation, testing, and review.
4. Shared memory preserves project context.
5. Generated artifacts are stored for future sessions.

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- Git

### Installation

```bash
git clone <repository-url>
cd Recuris
pip install -r requirements.txt
```

### Configuration

Configure:

- `crew.yaml`
- `llm_config.yaml`

### Run

```bash
python recuris.py
```

---

## Example Use Cases

- Generate application scaffolds
- Plan software architecture
- Review pull requests
- Generate technical documentation
- Coordinate autonomous engineering workflows
- Maintain long-running software projects

---

## Documentation

- `architecture.md`
- `getting-started.md`
- `api-reference.md`
- `contributing.md`
- `faq.md`
- `troubleshooting.md`

---

## Roadmap

### Current

- Multi-agent orchestration
- Shared memory
- Configurable LLM providers
- Task execution pipeline

### Planned

- GitHub integration
- IDE extensions
- Distributed agent execution
- Evaluation dashboard
- Plugin ecosystem

---

## Contributing

Contributions are welcome. Please open an issue before beginning major changes.

Documentation improvements, bug fixes, and feature proposals are all appreciated.

---

## License

MIT