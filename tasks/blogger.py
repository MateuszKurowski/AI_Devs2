from openai import OpenAI
from common.task_operation import Task_operation
from auth.config import OPEN_AI_API_KEY
import json

def main():
    try:
        task_name = "blogger"
        task_operation = Task_operation()

        json_response = task_operation.get_taks_info(task_name)

        hints = json_response.get("blog")

        system_prompt = f"""
Do podanych przez użytkownika tematów napisz krótkie, czterozdaniowe akapity na bloga.
###
Oczekiwany format odpowiedzi to JSON:
["tekst1","tekst2","tekst3"]
        """

        user_promt = "Tematy: \n"
        for hint in hints:
            user_promt += "- " + hint + "\n"

        client = OpenAI(
                api_key=OPEN_AI_API_KEY
            )
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_promt},
                      ]
        )
        task_operation.send_answer(json.loads(completion.choices[0].message.content))

    except Exception as e:
        print(f"Error occurred: {e}")