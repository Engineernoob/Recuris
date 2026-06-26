# Plugin SDK

## Overview

The Recuris Plugin SDK enables developers to extend the platform by creating custom agents, tools, integrations, and workflow components. Plugins allow Recuris to adapt to different engineering environments without modifying the core orchestration engine.

---

## Goals

The Plugin SDK is designed to:

- Extend Recuris without changing core code.
- Keep plugins isolated from one another.
- Provide stable interfaces for future compatibility.
- Encourage community-developed integrations.
- Support experimentation with new agent capabilities.

---

## Plugin Architecture

```text
                 Recuris
                    │
                    ▼
          Plugin Registration
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
 Agent Plugin   Tool Plugin   Integration Plugin
                    │
                    ▼
          Orchestration Engine
```

---

## Plugin Types

### Agent Plugins

Create new autonomous agents that participate in task execution.

Examples:

- Security Agent
- Database Agent
- DevOps Agent
- Accessibility Agent

### Tool Plugins

Expose reusable utilities that agents can invoke.

Examples:

- Git wrapper
- Docker runner
- Terminal executor
- Documentation generator

### Integration Plugins

Connect Recuris with external platforms.

Examples:

- GitHub
- GitLab
- Jira
- Slack
- Linear
- Notion

---

## Plugin Lifecycle

```text
Install Plugin
      │
      ▼
Register
      │
      ▼
Validate
      │
      ▼
Initialize
      │
      ▼
Execute
      │
      ▼
Shutdown
```

---

## Plugin Manifest

Each plugin should include metadata describing its capabilities.

Example:

```yaml
name: security-agent
version: 1.0.0
author: Example Developer
type: agent
entry: plugin.py
```

---

## Design Principles

- Stable public interfaces.
- Backward compatibility where possible.
- Sandboxed execution for plugins.
- Minimal coupling to the core platform.
- Explicit capability registration.

---

## Future Improvements

Planned enhancements include:

- Plugin marketplace
- Version compatibility checks
- Dependency management
- Digital plugin signing
- Automatic updates
- Plugin permission model
