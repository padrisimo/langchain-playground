from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from typing import Any, Dict


@tool
def web_search(query: str) -> str:
    """
    web search tool
    """
    duckduckgo_client = DuckDuckGoSearchRun()
    return duckduckgo_client.invoke(query)
