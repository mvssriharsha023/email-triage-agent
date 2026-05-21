from state import EmailAgentState

from storage.json_store import save_workflows

def storage_node(state: EmailAgentState):

    save_workflows(dict(state))

    return state