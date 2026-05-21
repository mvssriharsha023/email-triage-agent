from state import EmailAgentState
from models.llm import llm
from utils.loggers import logger

def urgency_detector_node(state: EmailAgentState) -> EmailAgentState:

    logger.info("Running urgency detector node")

    email = state["email"]

    prompt = f"""
    You are an email urgency detection system.

    Classify the urgency level into EXACTLY ONE:

    high
    medium
    low

    Guidelines:

    high:
    Production outages, security issues, critical failures,
    urgent customer-impacting problems, etc.

    medium:
    Important but non-critical operational issues.

    low:
    General inquiries, informational requests,
    non-urgent communication.

    Respond with ONLY:
    high
    medium
    or
    low

    Email:
    {email}
    """

    response = llm.invoke(prompt)

    urgency = response.content.strip().lower()
    
    logger.info(f"Email urgency classified as: {urgency}")

    state["urgency"] = urgency

    logger.info(f"Updated state: {state}")

    return state