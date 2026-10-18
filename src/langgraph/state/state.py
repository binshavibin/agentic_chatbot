from typing_extensions import TypedDict,List,Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represent the structure of the state use in graoh
    """
    messages:Annotated[List,add_messages]