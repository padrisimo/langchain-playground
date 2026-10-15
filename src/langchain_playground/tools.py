from langchain.agents import create_agent
from langchain.tools import tool

@tool
def print_document(name: str, content: str) -> str:
    """
    Print a document with the given name and content.

    Args:
        name (str): The name of the document.
        content (str): The content of the document.

    Returns:
        str: A confirmation message indicating that the document has been printed.
    """
    print(f"Document Name: {name}")
    print(f"Content: {content}")
    return f"Document '{name}' has been printed successfully." 