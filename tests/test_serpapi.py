import os

import pytest

from gtm_agents.mcp_server.server import search_serpapi


@pytest.mark.asyncio
async def test_serpapi_search():
    if not os.getenv("SERPAPI_API_KEY"):
        pytest.skip("SERPAPI_API_KEY is not configured")

    result = await search_serpapi(
        "B2B customer feedback software",
        num_results=3,
    )

    assert result["query"]
    assert result["source_count"] >= 1
    assert result["results"][0]["url"]

