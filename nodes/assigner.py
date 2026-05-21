from state import EmailAgentState
from utils.loggers import logger

def assigner_node(state: EmailAgentState):

    logger.info("Running assigner node")

    category = state["category"]

    assignment_map = {
        "technical": "Engineering Team",
        "billing": "Finance Team",
        "hr": "HR Team",
        "support": "Customer Support Team",
        "general": "Operations Team"
    }

    assigned_to = assignment_map.get(
        category,
        "Operations Team"
    )

    state["assigned_to"] = assigned_to

    logger.info(f"Email assigned to: {assigned_to}")

    logger.info(f"Updated state: {state}")
    
    return state