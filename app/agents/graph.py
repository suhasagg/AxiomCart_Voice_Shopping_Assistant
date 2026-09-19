from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from app.core.models import AgentState
from app.agents.nodes import orchestrator,product_agent,support_agent,synthesize

def route(s):
    return s['intent']
def build_graph():
    g=StateGraph(AgentState)
    for n,f in [('orchestrator',orchestrator),('product',product_agent),('support',support_agent),('synthesizer',synthesize)]: g.add_node(n,f)
    g.add_edge(START,'orchestrator')
    g.add_conditional_edges('orchestrator',route,{'product':'product','support':'support','both':'product'})
    g.add_edge('product','synthesizer'); g.add_edge('support','synthesizer'); g.add_edge('synthesizer',END)
    return g.compile(checkpointer=MemorySaver())
