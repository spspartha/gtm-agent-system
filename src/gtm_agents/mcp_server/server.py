import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("gtm-research-server")


def normalize_search_result(
    query: str,
    raw_results: list[dict[str, Any]],
) -> dict[str, Any]:
    results = []

    for item in raw_results:
        results.append(
            {
                "title": item.get("title", ""),
                "url": item.get("link", ""),
                "snippet": item.get("snippet", ""),
                "source": item.get("source", "serpapi"),
            }
        )

    return {
        "query": query,
        "results": results,
        "source_count": len(results),
    }


async def search_serpapi(
    query: str,
    num_results: int = 5,
) -> dict[str, Any]:
    api_key = os.getenv("SERPAPI_API_KEY")

    if not api_key:
        raise RuntimeError("SERPAPI_API_KEY is not configured")

    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": num_results,
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            "https://serpapi.com/search.json",
            params=params,
        )
        response.raise_for_status()
        payload = response.json()

    return normalize_search_result(
        query=query,
        raw_results=payload.get("organic_results", []),
    )


@mcp.tool()
async def search(
    query: str,
    num_results: int = 5,
) -> dict[str, Any]:
    """
    Search the web and return normalized results with source URLs.
    """
    if not query.strip():
        raise ValueError("query must not be empty")

    if not 1 <= num_results <= 10:
        raise ValueError("num_results must be between 1 and 10")

    return await search_serpapi(
        query=query,
        num_results=num_results,
    )


if __name__ == "__main__":
    mcp.run()

