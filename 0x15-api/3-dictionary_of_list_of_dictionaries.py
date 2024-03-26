#!/usr/bin/python3
'''uses REST API to get a TODO list progress for a given user'''
import requests
import sys
import json


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'

    users = requests.get(f'{url}/users').json()

    data = {}

    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')
        tasks = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos').json()
        data[user_id] = []

        for task in tasks:
            data[user_id].append({
                "username": user_name,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    with open('todo_all_employees.json', "w") as f:
        json.dump(data, f)
