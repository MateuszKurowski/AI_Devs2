from openai import OpenAI
from common.task_operation import Task_operation
from auth.config import OPEN_AI_API_KEY

def main():
    try:
        task_name = "moderation"
        task_operation = Task_operation()

        json_response = task_operation.get_taks_info(task_name)

        task_description = json_response.get("msg")
        # print(task_description)
        # print(json_response)

        sentences = json_response.get("input")

        result = []
        
        for sentence in sentences:
            client = OpenAI(
                api_key=OPEN_AI_API_KEY
            )
            moderation_response = client.moderations.create(input=sentence)
            output = moderation_response.results[0]
            if (output.flagged):
                result.append(1)
            else :
                result.append(0)

        task_operation.send_answer(result)

    except Exception as e:
        print(f"Error occurred: {e}")