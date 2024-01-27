from auth.authenticate  import authenticate 
from auth.config import OPEN_AI_API_KEY
from openai import OpenAI
from common.task_operation import Task_operation

def main():
    task_name = "functions"
    task_operation = Task_operation()
    json_response = task_operation.get_taks_info(task_name)

    json_data = {
        "name": "addUser",
        "description": "Add new user",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "provide name"
                },
                "surname": {
                    "type": "string",
                    "description": "provide surname"
                },
                "year": {
                    "type": "integer",
                    "description": "year of born"
                }
            }
        }
    }

    task_operation.send_answer(json_data)
