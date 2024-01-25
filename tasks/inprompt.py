from auth.authenticate  import authenticate 
from auth.config import OPEN_AI_API_KEY
from openai import OpenAI
from common.task_operation import Task_operation

def main():
    task_name = "inprompt"
    task_operation = Task_operation()
    answer = task_operation.get_taks_info(task_name)

    system_prompt = "Jesteś pomocnym asystentem. Z przesłanego przez użytkownika pytania zwróć imię o kim jest to pytanie. W odpowiedzi zwróć tylko imię i nic więcej."
    user_prompt = answer.get("question")

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
    name = completion.choices[0].message.content

    informations = answer.get("input", [])
    filtred_informations = [string for string in informations if name in string]

    system_prompt = f"""Jesteś pomocnym asystentem. Na podstawie poniższych informacji odpowiedz na przesłane przez użytkownika pytanie. 
    

    ### Informacje
    {filtred_informations}
    """

    print(system_prompt)
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
