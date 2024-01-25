from auth.authenticate  import authenticate 
from auth.config import OPEN_AI_API_KEY
from openai import OpenAI
from common.task_operation import Task_operation

def main():
    try:
        task_name = "embedding"
        task_operation = Task_operation()

        json_response = task_operation.get_taks_info(task_name)
        sentance = "Hawaiian pizza"

        client = OpenAI(
                api_key=OPEN_AI_API_KEY
            )
        completion = client.embeddings.create(
            model="text-embedding-ada-002",
            input=sentance,
        )

        task_operation.send_answer(completion.data[0].embedding)

    except Exception as e:
        print(f"Error occurred: {e}")

   


