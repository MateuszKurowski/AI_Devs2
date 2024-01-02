from common.task_operation import Task_operation
import json

def main():
    try:
        task_name = "helloapi"
        task_operation = Task_operation()

        json_response = task_operation.get_taks_info(task_name)

        task_description = json_response.get("msg")
        # print(task_description)

        answer = {"answer": json_response.get("cookie")}
        response = task_operation.send_answer(answer)
        print(f"Status: {response.get('note')}")
        print(response)

    except Exception as e:
        print(f"Error occurred: {e}")

   


