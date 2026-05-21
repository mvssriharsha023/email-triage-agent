import json
import os

STORAGE_FILE = "storage/workflows.json"

def load_workflows():

    if not os.path.exists(STORAGE_FILE):
        return {}

    with open(STORAGE_FILE, "r") as file:
        return json.load(file)
    
def save_workflows(workflow_data):

    workflows = load_workflows()

    workflows.append(workflow_data)

    with open(STORAGE_FILE, "w") as file:
        json.dump(workflows, file, indent=4)