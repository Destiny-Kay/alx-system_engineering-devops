#!/usr/bin/python3
'''uses REST API to get a TODO list progress for a given user'''
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'

    user = requests.get(f'{url}/users/{id}').json()
    todo = requests.get(f'{url}/todos', params={"userId": id}).json()

    tasks = [i["title"] for i in todo if i["completed"]]
    print(f"Employee {user.get('name')} is done with ", end="")
    print(f"tasks({len(tasks)}/{len(todo)}):")
    [print(f"\t {i}") for i in tasks]
