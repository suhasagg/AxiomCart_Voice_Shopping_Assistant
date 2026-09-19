from typing import TypedDict, Annotated, Literal
from pydantic import BaseModel, Field
import operator

class Product(BaseModel):
    sku:str; name:str; category:str; price:float; description:str; stock:int=0
class ChatRequest(BaseModel):
    thread_id:str; user_id:str; message:str; approved:bool=False
class AgentState(TypedDict, total=False):
    thread_id:str; user_id:str; message:str; intent:str
    products:list[dict]; support:list[str]; cart:list[dict]
    product_answer:str; support_answer:str; answer:str
    needs_approval:bool; approved:bool
    events:Annotated[list[str], operator.add]
