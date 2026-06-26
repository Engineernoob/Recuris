# Shared Memory

## Overview

Recuris uses a shared memory layer to preserve project context across autonomous agents and multiple execution sessions. Instead of treating each task as an isolated interaction, agents can retrieve relevant knowledge generated during previous work.

This shared context enables more consistent planning, implementation, documentation, and review over the lifetime of a software project.

---

## Memory Architecture

```text
              User Task
                  │
                  ▼
          Orchestration Engine
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Architect    Engineer    Reviewer
     │            │            │
     └────────────┼────────────┘
                  ▼
          Shared Memory Layer
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 Project Data  Vector Store  Artifacts
```

---

## What Is Stored?

The shared memory layer may contain:

- Project requirements
- Task history
- Architecture decisions
- Code summaries
- Documentation
- Agent outputs
- Review feedback
- Generated artifacts
- Repository metadata

Keeping this information centralized allows agents to build on previous work instead of repeating it.

---

## Memory Types

### Short-Term Memory

Maintains context for the current execution, including active tasks, intermediate reasoning, and temporary workflow state.

### Long-Term Memory

Stores durable project knowledge that should persist across sessions, such as architectural decisions, completed work, documentation, and historical context.

### Semantic Memory

Embeddings stored in a vector database enable similarity search, allowing agents to retrieve relevant information based on meaning rather than exact keywords.

---

## Retrieval Workflow

```text
New Task
    │
    ▼
Generate Query
    │
    ▼
Semantic Search
    │
    ▼
Retrieve Relevant Context
    │
    ▼
Augment Agent Prompt
    │
    ▼
Execute Task
```

---

## Design Principles

- Preserve important project knowledge.
- Minimize duplicate work.
- Share context across agents.
- Separate transient and persistent memory.
- Support retrieval before generation.
- Keep memory modular and extensible.

---

## Future Improvements

Planned enhancements include:

- Memory versioning
- Automatic summarization
- Repository-wide indexing
- Cross-project knowledge sharing
- Memory quality evaluation
- Human feedback integration
