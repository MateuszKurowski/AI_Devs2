import requests
import json
from auth.authenticate  import authenticate 

class Task_operation:
    def __init__(self):
        pass

    @property
    def token(self):
        return self._token

    def get_taks_info(self, task_name):
        token = authenticate(task_name)
        self._token = token
        if token == None:
            return None

        url = "https://zadania.aidevs.pl/task/" + token 
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            json_response = response.json()
            code = json_response.get("code")

            if code == 0:
                print()
                print("Treść zadania: ")
                print(json.dumps(json_response, indent=4))
                print()
                print("-----------------------------------------------------------------------")
                print()
                return json_response
            else:
                raise Exception(f"Task download error ({code}): {json_response}")

        except requests.exceptions.RequestException as e:
            print(f"Authentication error: {e}")

    def get_taks_info_with_data(self, task_name, data):
        token = authenticate(task_name)
        self._token = token
        if token == None:
            return None

        url = "https://zadania.aidevs.pl/task/" + token 

        try:
            response = requests.post(url, data=data)

            json_response = response.json()
            code = json_response.get("code")

            json_response = response.json()
            answer = json_response.get("answer")

            if answer != "":
                print()
                print("Treść zadania: ")
                print(json.dumps(json_response, indent=4))
                print()
                print("-----------------------------------------------------------------------")
                print()
                return answer
            else: 
                raise Exception(f"Task download error ({response.status_code}): {json_response}")

        except requests.exceptions.RequestException as e:
            print(f"Authentication error: {e}")

    def send_answer(self, answer):
        url = "https://zadania.aidevs.pl/answer/" + self._token
        headers = {"Content-Type": "application/json"}

        try:
            data = {"answer": answer}
            print("Ciało zapytania:")
            print(data)
            print()
            print("-----------------------------------------------------------------------")
            print()
            response = requests.post(url, headers=headers, data=json.dumps(data))
            #response.raise_for_status()

            json_response = response.json()
            code = json_response.get("code")

            if code == 0:
                print("Odpowiedź: ")
                print(json.dumps(json_response, indent=4))
                print()
                print("-----------------------------------------------------------------------")
                print()
            else:
                raise Exception(f"Task answer error: {json_response.get('msg')} ({code}) - {json_response}")

        except requests.exceptions.RequestException as e:
            print(f"Answer error: {e}")

