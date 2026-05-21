from typing import TypedDict, List, Optional

__all__ = ["EmailAgentState"]

class EmailAgentState(TypedDict):

    email: str

    is_spam: Optional[bool]

    category: Optional[str]

    urgency: Optional[str]

    tasks: Optional[List[str]]

    assigned_to: Optional[str]

    response_draft: Optional[str]

    human_approved: Optional[bool]

    final_response: Optional[str]

    sent: Optional[bool]