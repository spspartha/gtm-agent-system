import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    openai_api_key: str | None
    serpapi_api_key: str | None
    mcp_host: str
    mcp_port: int


def load_settings() -> Settings:
    port = int(os.getenv("MCP_PORT", "8000"))

    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        serpapi_api_key=os.getenv("SERPAPI_API_KEY"),
        mcp_host=os.getenv("MCP_HOST", "127.0.0.1"),
        mcp_port=port,
    )

