from state import EmailAgentState
from models.llm import llm
from utils.loggers import logger

def responder_node(state: EmailAgentState):

    logger.info("Running responder node")

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

    logger.info(f"Generated response draft: {reply}")

    state["response_draft"] = reply

    state["sent"] = False

    state["human_approved"] = False

    state["final_response"] = None

    logger.info(f"Updated state: {state}")

    return state