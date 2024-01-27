from auth.authenticate  import authenticate 
from auth.config import OPEN_AI_API_KEY
from openai import OpenAI
import requests
import time
import os
from common.task_operation import Task_operation
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

def main():
    task_name = "scraper"
    task_operation = Task_operation()
    json_response = task_operation.get_taks_info(task_name)

    file_path = os.path.join(os.getcwd(), 'dokument.txt')  
    link = json_response.get('input')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    context = ""
    while True:
        try:
            response = requests.get(link, headers= headers)
            response.raise_for_status()
            context = response.content
            break
        except requests.exceptions.RequestException as e:
            print(f'Wystąpił błąd podczas pobierania pliku wiedzy. Treść: {e}')
            print('Ponawiam próbę pobrania...')
            time.sleep(1)

    system_prompt = f'''
        Korzystając z dostarczonego kontekstu odpowiedz na pytanie użytkownika. Odpowiedz po polsku, odpowiedź ma być krótka i zwięzła.

        ### Kontekst
        {context}
    '''
    user_prompt = json_response.get('question')

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

    input()
    os.remove(file_path)