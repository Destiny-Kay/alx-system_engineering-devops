#!/usr/bin/python3
'''uses REST API to get a TODO list progress for a given user'''
import requests
import sys
import json


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'

    user = requests.get(f'{url}/users/{id}').json()
    todo = requests.get(f'{url}/todos', params={"userId": id}).json()

    file = f"{id}.json"
    dicts = {id: []}
    for task in todo:
        dicts[id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    with open(file, "w") as f:
        json.dump(dicts, f)
