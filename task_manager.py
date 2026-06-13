import json
import os

DATA_FILE = "data/tasks.json"

tasks = []



def load_tasks():
    global tasks
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            tasks = json.load(f)
    else:
        tasks = []


def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# ➕ Ajouter une tâche
def add_task(task):
    task = task.strip()
    if task:
        tasks.append(task)
        save_tasks()


def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()


def get_tasks():
    return tasks