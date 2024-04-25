#!/usr/bin/python3
"""
task 1
"""
import requests
import sys


def save_to_csv(id):
    """save func"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{id}"

    response = requests.get(user_url)
    user_data = response.json()

    name = user_data['username']
 
    todo_url = f"{url}/todos?userId={id}"

    response = requests.get(todo_url)
    todos_data = response.json()

    csv_filename = f"{id}.csv"

    with open(csv_filename, "w", newline='') as csvfile:
        for todo in todos_data:
            completed = "True" if todo['completed'] else "False"
            title = todo['title']
            csvfile.write(f'"{id}","{name}","{completed}","{title}"\n')


if __name__ == "__main__":
    id = int(sys.argv[1])
    save_to_csv(id)
