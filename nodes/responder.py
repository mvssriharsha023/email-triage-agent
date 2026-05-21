from state import EmailAgentState
from models.llm import llm


def responder_node(state: EmailAgentState):

    email = state["email"]

    category = state.get("category")

    urgency = state.get("urgency")

    tasks = state.get("tasks", [])

    assigned_to = state.get("assigned_to")


    prompt = f"""
    You are a professional enterprise email assistant.

    Generate a concise professional reply.

    Context:

    Category: {category}

    Urgency: {urgency}

    Tasks:
    {tasks}

    Assigned Team:
    {assigned_to}

    Original Email:
    {email}

    Rules:
    - Keep response professional
    - Keep response concise
    - Acknowledge the issue/request
    - Mention assignment if applicable
    - Do not hallucinate fake details
    """


    response = llm.invoke(prompt)

    reply = response.content.strip()

    state["response_draft"] = reply

    return state