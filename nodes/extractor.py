from state import EmailAgentState
from models.llm import llm
from utils.loggers import logger

def extractor_node(state: EmailAgentState):

    logger.info("Running extractor node")

    email = state["email"]

    prompt = f"""
    You are an AI task extraction system.

    Extract all actionable tasks from the email.

    Rules:
    - Return ONLY actionable tasks
    - Keep tasks short and clear
    - One task per line
    - If no tasks exist, respond with:
      NO_TASKS

    Email:
    {email}
    """

    response = llm.invoke(prompt)

    result = response.content.strip()

    logger.info(f"Extracted tasks: {result}")

    if result == "NO_TASKS":
        state["tasks"] = []
    else:
        tasks = result.split("\n")

        cleaned_tasks = [
            task.strip("- ").strip()
            for task in tasks
            if task.strip()
        ]

        state["tasks"] = cleaned_tasks
    
    logger.info(f"Updated state: {state}")

    return state