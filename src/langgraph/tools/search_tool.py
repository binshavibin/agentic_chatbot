from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns the list of tools to be used in chatbot
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tools_node(tools):
    """
    Create and returns a tools node for the graph
    """
    return ToolNode(tools=tools)