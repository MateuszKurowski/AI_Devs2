from auth.authenticate  import authenticate 
from auth.config import OPEN_AI_API_KEY
from openai import OpenAI
from common.task_operation import Task_operation

def main():
    task_name = "liar"
    data = {"question": "What is capital of Poland?"}
    task_operation = Task_operation()

    answer = task_operation.get_taks_info_with_data(task_name, data)

    system_prompt = """Jesteś asystentem do sprawdzania czy odpowiedzi na dane  pytanie są na temat. Zweryfikuj podaną przez użytkownika odpowiedź czy jest ona powiązana z tematem pytania. Jeżeli jest na temat i odpowiedź ma sens zwróć \"YES\" i nic więcej, natomiast jeżeli odpowiedź jest nie na temat to zwróć \"NO\" i nic więcej.
    Pytanie to: \"What is capital of Poland?\""""

    user_prompt = f"Answer: {answer}"

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
