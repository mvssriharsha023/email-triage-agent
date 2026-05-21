from langgraph.graph import StateGraph, START, END

from state import EmailAgentState
from nodes.spam_checker import spam_checker_node
from nodes.classifier import classifier_node
from nodes.urgency_detector import urgency_detector_node
from nodes.extractor import extractor_node
from nodes.assigner import assigner_node
from nodes.responder import responder_node
from nodes.storage_node import storage_node

graph_builder = StateGraph(EmailAgentState)

graph_builder.add_node("spam_checker", spam_checker_node)
graph_builder.add_node("classifier", classifier_node)
graph_builder.add_node("urgency_detector", urgency_detector_node)
graph_builder.add_node("extractor", extractor_node)
graph_builder.add_node("assigner", assigner_node)
graph_builder.add_node("responder", responder_node)
graph_builder.add_node("storage", storage_node)

graph_builder.add_edge(START, "spam_checker")

def route_after_spam_check(state: EmailAgentState):
    if state.get("is_spam"):
        return "storage"
    
    return "classifier"

def route_after_task_extraction(state: EmailAgentState):
    tasks = state.get("tasks", [])
    if not tasks:
        return "storage"
    
    return "assigner"

graph_builder.add_conditional_edges("spam_checker", route_after_spam_check)

graph_builder.add_edge("classifier", "urgency_detector")

graph_builder.add_edge("urgency_detector", "extractor")

graph_builder.add_conditional_edges("extractor", route_after_task_extraction)

graph_builder.add_edge("assigner", "responder")

graph_builder.add_edge("responder", "storage")

graph_builder.add_edge("storage", END)

graph = graph_builder.compile()