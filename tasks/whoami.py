from auth.config import OPEN_AI_API_KEY
from common.task_operation import Task_operation
from openai import OpenAI
import time

def main():
    task_name = "whoami"
    task_operation = Task_operation()

    hints = []

    for i in range(10):
        json_response = task_operation.get_taks_info(task_name)
        hint = json_response.get('hint')
        if hint not in hints:
            hints.append(hint)
        time.sleep(5)
        

    system_prompt = 'Jesteś pomocnym asystentem który na podstawie ciekawostek zwróconych przez użytkownika zgadujesz jaka to osoba. Zwróć imię i nazwisko zgadywanej osoby i nic więcej, nie dodawaj żadnego komentarza.'
    user_prompt = ''
    for i in range(len(hints)):
        user_prompt += f'\n {i}. {hints[i]}'

    client = OpenAI(
                api_key=OPEN_AI_API_KEY
            )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
                ]
    )

    task_operation.send_answer(completion.choices[0].message.content)