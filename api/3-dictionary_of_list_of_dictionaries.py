#!/usr/bin/python3
"""
task 2
"""
import json
import requests


def save_to_json():
    """save func"""
    url = "https://jsonplaceholder.typicode.com"

    todos_url = f"{url}/todos"
    users_url = f"{url}/users"

    response = requests.get(todos_url)
    todos_data = response.json()
    tasks = {}

    response = requests.get(users_url)
    user_data = response.json()

    dict = {}

    for user in user_data:
        id = user['id']
        todos = requests.get(f"{todos_url}?userId={id}").json()
        user_list = []

        for todo in todos:
            user_list.append(
                    {
                        "username": user['username'],
                        "task": todo['title'],
                        "completed": todo['completed'],
                    }
                )
            dict[user['id']] = user_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict, file)


if __name__ == "__main__":
    save_to_json()
