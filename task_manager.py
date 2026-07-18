import storage

tasks = []



def load_tasks():
    global tasks
    task_objects = storage.load_tasks_from_markdown(include_completed=False)
    tasks = [task.title for task in task_objects]


def add_task(task):
    task = task.strip()
    if task:
        storage.append_task_to_markdown(task)
        load_tasks()


def remove_task(index):
    if storage.remove_task_by_index(index, include_completed=False):
        load_tasks()


def get_tasks():
    return tasks.copy()