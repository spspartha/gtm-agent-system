from gtm_agents.mcp_server.server import normalize_search_result


def test_normalize_search_result():
    result = normalize_search_result(
        "test query",
        [
            {
                "title": "Example",
                "link": "https://example.com",
                "snippet": "Example result",
            }
        ],
    )

    assert result["query"] == "test query"
    assert result["source_count"] == 1
    assert result["results"][0]["url"] == "https://example.com"

