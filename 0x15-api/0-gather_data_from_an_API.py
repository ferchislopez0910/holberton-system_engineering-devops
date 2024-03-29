#!/usr/bin/python3
import requests
from sys import argv
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """


if __name__ == "__main__":
    """
    function to get employees todo list
    progress
    """
    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    tasks = []
    for task in todo:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(tasks), len(todo)))
    for task in tasks:
        print("\t {}".format(task))
