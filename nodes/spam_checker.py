from state import EmailAgentState
from models.llm import llm
from utils.loggers import logger

def spam_checker_node(state: EmailAgentState):

    logger.info("Running spam checker node")
    
    email = state["email"]

    prompt = f"""
    You are a spam detection system.

    Analyze the following email and determine if it is spam or not.

    Respond with ONLY:
    SPAM
    or
    NOT_SPAM

    Email:
    {email}
    """

    response = llm.invoke(prompt)

    result = response.content.strip()

    logger.info(f"Spam classification result: {result}")

    if result == "SPAM":
        state["is_spam"] = True
    else:
        state["is_spam"] = False

    logger.info(f"Updated state: {state}")
    
    return state