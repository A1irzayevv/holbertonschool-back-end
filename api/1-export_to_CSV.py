#!/usr/bin/python3
"""
first rest api code
"""
import requests
import sys


def get_todo_rest_api(id):
    """request function"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{id}"

    response = requests.get(user_url)
    user_data = response.json()

    name = user_data['name']

    todo_url = f"{url}/todos?userId={id}"

    response = requests.get(todo_url)
    todos_data = response.json()

    csv_filename = f"{id}.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        for todo in todos_data:
            task_completed = 'True' if todo['completed'] else 'False'
            title = todo['title']
            csvfile.write(f'"{id}","{name}","{task_completed}","{title}"\n')


if __name__ == "__main__":
    id = int(sys.argv[1])
    get_todo_rest_api(id)
