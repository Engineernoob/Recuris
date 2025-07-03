# Recuris Project

## Overview
Recuris is a multi-agent system for software development, featuring specialized agents that collaborate to complete software projects.

## Project Structure

### Core Components
- `agents/`: Contains specialized agent implementations (Architect, Engineer, QA, etc.)
- `core/`: Core system components including task management, messaging, and workspace
- `data/`: Contains memory files and output from previous sessions

### Key Files
- `recuris.py`: Main entry point
- `crew.yaml`: Agent configuration
- `llm_config.yaml`: LLM settings

## Getting Started

### Prerequisites
- Python 3.8+
- Required packages (install via `pip install -r requirements.txt`)

### Usage
1. Configure agents in `crew.yaml`
2. Set up LLM configuration in `models/llm_config.yaml`
3. Run main script: `python recuris.py`

## Features
- Multi-agent collaboration
- Task decomposition and execution
- Memory persistence between sessions
- Quality assurance integration

## Documentation
- See `architecture.md` for system design details
- Agent-specific documentation in their respective files

## Contributing
Pull requests are welcome. For major changes, please open an issue first.

## License
[MIT](https://choosealicense.com/licenses/mit/)
