from state import EmailAgentState


def assigner_node(state: EmailAgentState):

    tasks = state.get("tasks", [])

    # if not tasks:
    #     state["assigned_to"] = None
    #     return state

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

    return state