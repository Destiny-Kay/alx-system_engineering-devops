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

    file = f"{id}.csv"
    with open(file, "w") as f:
        for item in todo:
            f.write(
                f'"{id}","{user["username"]}","{item["completed"]}",\
                    "{item["title"]}"\n'
            )
