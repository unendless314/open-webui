import logging
from typing import Optional

import requests
from fastapi import HTTPException

from open_webui.retrieval.web.main import SearchResult, get_filtered_results
from open_webui.env import SRC_LOG_LEVELS

log = logging.getLogger(__name__)
log.setLevel(SRC_LOG_LEVELS["RAG"])


def search_brave(
    api_key: str, query: str, count: int, filter_list: Optional[list[str]] = None
) -> list[SearchResult]:
    """Search using Brave's Search API and return the results as a list of SearchResult objects.

    Args:
        api_key (str): A Brave Search API key
        query (str): The query to search for
    """
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key,
    }
    params = {"q": query, "count": count}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code == 429:
            raise HTTPException(
                status_code=429, detail="Brave API rate limit exceeded"
            ) from e

        status_code = e.response.status_code if e.response else 500
        raise HTTPException(
            status_code=status_code, detail=f"Brave API request failed: {e}"
        ) from e

    json_response = response.json()
    results = json_response.get("web", {}).get("results", [])
    if filter_list:
        results = get_filtered_results(results, filter_list)

    return [
        SearchResult(
            link=result["url"],
            title=result.get("title"),
            snippet=result.get("description"),
        )
        for result in results[:count]
    ]
