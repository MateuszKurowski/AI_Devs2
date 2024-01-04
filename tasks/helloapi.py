from common.task_operation import Task_operation

def main():
    try:
        task_name = "helloapi"
        task_operation = Task_operation()

        json_response = task_operation.get_taks_info(task_name)

        task_operation.send_answer(json_response.get("cookie"))

    except Exception as e:
        print(f"Error occurred: {e}")

   


