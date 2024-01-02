import sys
sys.path.append("F:\\Projects\\AI_Devs2\\auth")

from config import AI_DEVS_API_KEY
import requests
import json

def authenticate (task_name):
    url = "https://zadania.aidevs.pl/token/" + task_name
    headers = {"Content-Type": "application/json"}
    data = {"apikey": AI_DEVS_API_KEY}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        json_response = response.json()
        code = json_response.get("code")
        
        if code == 0:
            return json_response.get("token")
        else:
            raise Exception(f"Authentication error: {json_response.get('message')} (Code: {code}) - {json_response}")

    except requests.exceptions.RequestException as e:
        print(f"Authentication error: {e}")
        return None