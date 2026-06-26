# System Diagrams

This document contains high-level diagrams that illustrate how PatchPilot processes incidents from submission through AI analysis.

---

## System Overview

```text
                Developer
                    │
                    ▼
          Next.js Web Application
                    │
                    ▼
              FastAPI Backend
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
 Evidence Parser  AI Pipeline   PostgreSQL
     │              │              │
     └──────────────┼──────────────┘
                    ▼
           Analysis Results API
                    │
                    ▼
             Results Dashboard
```

---

## Incident Processing Flow

```text
Create Incident
      │
      ▼
Upload Evidence
      │
      ▼
Validate Request
      │
      ▼
Normalize Evidence
      │
      ▼
Extract Signals
      │
      ▼
Run AI Analysis
      │
      ▼
Generate Summary
      │
      ▼
Rank Root Causes
      │
      ▼
Generate Suggested Fixes
      │
      ▼
Store Results
      │
      ▼
Display Dashboard
```

---

## Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| Next.js Frontend | Incident creation, uploads, and visualization |
| FastAPI Backend | API orchestration and business logic |
| Evidence Parser | Normalize and extract debugging signals |
| AI Pipeline | Generate summaries, hypotheses, and fixes |
| PostgreSQL | Persist incidents and analysis results |
| Ollama | Execute local language model inference |

---

## Data Flow

```text
Logs
Stack Traces
Screenshots
Bug Reports
      │
      ▼
Evidence Parser
      │
      ▼
Structured Signals
      │
      ▼
AI Pipeline
      │
      ▼
Engineering Artifacts

• Incident Summary
• Root-Cause Hypotheses
• Suggested Fixes
• Commit Message
• Pull Request Summary
```

---

## Future Diagrams

As PatchPilot evolves, this document can be expanded with:

- Sequence diagrams
- Deployment diagrams
- Database ER diagrams
- Authentication flow
- GitHub integration flow
- Multi-agent AI workflow
- Evaluation pipeline
