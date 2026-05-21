from state import EmailAgentState
from utils.loggers import logger
from storage.json_store import save_workflows

def storage_node(state: EmailAgentState):

    logger.info("Running storage node")

    save_workflows(dict(state))

    logger.info("State saved to storage successfully")

    return state