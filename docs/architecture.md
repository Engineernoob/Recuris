# Architecture

## Overview

Recuris is an AI-native software engineering platform composed of specialized autonomous agents that collaborate to plan, build, test, document, and maintain software projects. The architecture emphasizes modularity, deterministic orchestration, and extensibility while allowing AI agents to operate within well-defined responsibilities.

---

## System Architecture

```text
                    User
                     │
                     ▼
               Web Dashboard / CLI
                     │
                     ▼
             Orchestration Engine
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
 Planning Agent   Coding Agent   Review Agent
     │               │                │
     └───────────────┼────────────────┘
                     ▼
              Shared Knowledge Layer
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     PostgreSQL   Vector DB   File Storage
```

---

## Core Components

### Web Dashboard

Provides project management, agent monitoring, conversation history, task visualization, and execution controls.

### CLI

Offers developers a lightweight interface for creating tasks, reviewing execution logs, and interacting with Recuris directly from the terminal.

### Orchestration Engine

Coordinates communication between autonomous agents, schedules work, tracks execution state, and manages retries and workflow dependencies.

### AI Agents

Each agent owns a specific responsibility.

Examples include:

- Planning
- Coding
- Code Review
- Documentation
- Testing
- Debugging
- Deployment

This separation keeps prompts focused while reducing cross-agent interference.

---

## Data Layer

Recuris combines multiple storage systems:

- PostgreSQL for structured application data.
- Vector database for semantic memory and retrieval.
- File storage for project artifacts and generated assets.

---

## Design Principles

- Modular services with clear boundaries.
- Strong separation between orchestration and execution.
- Shared memory across autonomous agents.
- Extensible plugin architecture.
- Human approval for critical actions.
- Deterministic workflows wherever possible.

---

## Future Architecture

Planned capabilities include:

- Multi-agent collaboration across repositories.
- Distributed execution.
- Team workspaces.
- GitHub and GitLab integrations.
- IDE extensions.
- Evaluation dashboards.
- Autonomous long-running workflows.