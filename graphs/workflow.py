from langgraph.graph import StateGraph, START, END

from state import EmailAgentState
from nodes.spam_checker import spam_checker_node
from nodes.classifier import classifier_node

graph_builder = StateGraph(EmailAgentState)

graph_builder.add_node("spam_checker", spam_checker_node)
graph_builder.add_node("classifier", classifier_node)

graph_builder.add_edge(START, "spam_checker")

def route_after_spam_check(state: EmailAgentState):
    if state.get("is_spam"):
        return END
    
    return "classifier"

graph_builder.add_conditional_edges("spam_checker", route_after_spam_check)

graph_builder.add_edge("classifier", END)

graph = graph_builder.compile()