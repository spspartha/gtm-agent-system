# GTM Agent System

A multi-agent Go-To-Market (GTM) strategy system powered by CrewAI and MCP (Model Context Protocol). This system leverages specialized agents to perform market research and generate comprehensive project briefs.

## System Overview

The system utilizes CrewAI to orchestrate autonomous agents. The primary research capabilities are extended through a custom Search Tool that interfaces with an MCP server.

## Installation & Setup

### Prerequisites
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

### Environment Configuration
1. Clone the repository to `/home/ubuntulab01/gtm-agent-system`.
2. Ensure your `.env` file contains the necessary API keys (e.g., OpenAI, Serper, etc.).

### Installation
```bash
cd /home/ubuntulab01/gtm-agent-system
uv sync
```

## Architecture

### Agents
- **Research Agent**: Conducts deep-dive market analysis using the `ResearchSearchTool`.
- **Strategy Agent**: Synthesizes research into actionable GTM plans.

### Tools
The system features a custom `ResearchSearchTool` located in `src/gtm_agents/tools.py`. This tool is built on the `crewai.tools.BaseTool` class to ensure compatibility with CrewAI's Pydantic validation.

#### MCP Integration
The tool acts as a bridge to an MCP server, executing searches via an asynchronous bridge:
- **Location**: `src/gtm_agents/mcp_server/server.py`
- **Execution**: Managed via `asyncio.run()` within the tool's `_run` method to provide a synchronous interface for the agents.

## Usage

To execute the GTM crew and generate a strategy:

```bash
uv run main.py
```

## Troubleshooting

### Pydantic Validation Errors
If you encounter `pydantic_core._pydantic_core.ValidationError` related to `BaseTool`, ensure your custom tools import from `crewai.tools` rather than `langchain_core.tools`:

```python
# Correct Import
from crewai.tools import BaseTool
```

### IncompleteFieldDefinitionWarning
The warning regarding `lifespan` unresolved forward references is a known Pydantic/dependency warning and does not impact the execution of the agents.

## Project Structure
- `main.py`: Entry point for the application.
- `src/gtm_agents/crew.py`: Crew configuration and task definitions.
- `src/gtm_agents/agents.py`: Agent definitions and tool assignments.
- `src/gtm_agents/tools.py`: Custom CrewAI tools.
- `src/gtm_agents/mcp_server/`: MCP server implementation for external tool integration.
