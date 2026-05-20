from state import EmailAgentState
from models.llm import llm

def classifier_node(state: EmailAgentState) -> EmailAgentState:
    email = state["email"]

    prompt = f"""
    You are an email classification system.

    Classify the email into ONE of these categories only:

    Categories:

    technical:
    Server issues, bugs, system failures, engineering problems.

    billing:
    Payments, invoices, refunds, subscriptions, transactions.

    hr:
    Leave requests, hiring, employee matters.

    support:
    General customer help requests unrelated to billing.

    general:
    Anything else.


    Respond with ONLY the category name.

    Email:
    {email}
    """

    response = llm.invoke(prompt)

    category = response.content.strip().lower()

    state["category"] = category

    return state