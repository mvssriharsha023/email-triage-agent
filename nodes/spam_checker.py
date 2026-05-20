from state import EmailAgentState
from models.llm import llm

def spam_checker_node(state: EmailAgentState):
    
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

    if result == "SPAM":
        state["is_spam"] = True
    else:
        state["is_spam"] = False
    
    return state