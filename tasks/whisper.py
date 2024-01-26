from auth.authenticate  import authenticate 
from auth.config import OPEN_AI_API_KEY
import openai
from common.task_operation import Task_operation
import re
import requests
import os
import time
import numpy as np

def main():
    task_name = "whisper"
    task_operation = Task_operation()
    json_response = task_operation.get_taks_info(task_name)

    regex = re.compile(r'https://\S+')
    link = regex.findall(json_response.get('msg'))
    response = requests.get(link[0])
    audio_content = response.content
    file_path = os.path.join(os.getcwd(), 'audio.mp3')   

    with open(file_path, 'wb') as file:
        file.write(audio_content)
    
    with open(file_path, 'rb') as file:
        openai.api_key = OPEN_AI_API_KEY
        transcryption = openai.audio.transcriptions.create(model='whisper-1', file=file)
        
        task_operation.send_answer(transcryption.text)

    os.remove(file_path)