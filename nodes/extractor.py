from state import EmailAgentState
from models.llm import llm


def extractor_node(state: EmailAgentState):

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

    return state