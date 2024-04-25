#!/usr/bin/python3
"""
task 2
"""
import json
import requests
import sys


def save_to_json(id):
    """save func"""
    url = "https://jsonplaceholder.typicode.com"

    user_url = f"{url}/users/{id}"

    response = requests.get(user_url)
    user_data = response.json()
    name = user_data['username']

    todos_url = f"{url}/todos?userId={id}"

    response = requests.get(todos_url)
    todos_data = response.json()

    json_data = {
            str(id): [
                {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": name
                }
                for todo in todos_data
            ]
        }

    json_filename = f"{id}.json"

    with open(json_filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = sys.argv[1]
        save_to_json(id)
