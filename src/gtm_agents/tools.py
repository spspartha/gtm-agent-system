# src/gtm_agents/tools.py

from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

from gtm_agents.mcp_server.server import search


class ResearchSearchInput(BaseModel):
    query: str = Field(..., description="The web search query")


class ResearchSearchTool(BaseTool):
    name: str = "research_search"
    description: str = (
        "Searches the web for current market research information "
        "and returns normalized results with sources."
    )
    args_schema: Type[BaseModel] = ResearchSearchInput

    def _run(self, query: str) -> str:
        return search_sync(query)


def search_sync(query: str) -> str:
    """
    Synchronous wrapper around the async search function.
    """
    import asyncio

    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(search(query))

    # This path is generally unnecessary for normal CrewAI execution.
    # If your MCP search function is already synchronous, call it directly.
    return asyncio.run(search(query))


# Change this import
#from langchain_core.tools import BaseTool
# Keep the rest as is
#from gtm_agents.mcp_server.server import search_serpapi
#import asyncio

#class ResearchSearchTool(BaseTool):
#    name: str = "search_tool"
#    description: str = (
#        "Searches the web for market research and GTM planning information. "
#        "Use this tool to find competitors, trends, and customer pain points."
#    )
#
#    def _run(self, query: str) -> str:
#        # Since CrewAI agents run in a synchronous environment, 
#        # we wrap the async MCP function here.
#        return asyncio.run(search_serpapi(query))
