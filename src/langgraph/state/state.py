from typing_extensions import TypedDict,list,Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represent the structure of the state use in graoh
    """
    messages:Annotated[list,add_messages]