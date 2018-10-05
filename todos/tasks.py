from datetime import datetime

from .exceptions import (
    InvalidTaskStatus, TaskAlreadyDoneException, TaskDoesntExistException)
from .utils import parse_date, parse_int, serialize


def new():
    return []


def create_task(tasks, name, description=None, due_on=None):
    if due_on and type(due_on) != datetime:
        due_on = parse_date(due_on)
    
    task = {}
    task['task'] = name
    task['description'] = description
    task['due_on'] = due_on
    task['status'] = 'pending'
    return tasks.append(task)



def list_tasks(tasks, status='all'):
    if status not in ('all', 'done', 'pending'):
        raise InvalidTaskStatus()
    result = []
    for task_id, task in enumerate(tasks, start = 1):
        content = (task_id, task['task'], task['due_on'].strftime('%Y-%m-%d %H:%M:%S'), task['status'])
        if status == task['status'] or status == 'all':
            result.append(content)
    return result

def complete_task(tasks, name):
    tasks_updated = []
    id_name = parse_int(name)
    
    for task_id, task in enumerate(tasks, start=1):
        if task['task'] == name or task_id == id_name:
            task = task.copy()
            if task['status'] == 'done':
                raise TaskAlreadyDoneException()
            task['status'] = 'done'
        tasks_updated.append(task)
    if tasks == tasks_updated:
        raise TaskDoesntExistException()
    return tasks_updated