import json
from datetime import datetime
from .exceptions import InvalidTaskDueDateException


def parse_date(date_str):
    formats = [
        '%Y-%m-%d',
        '%Y-%m-%d %H:%M:%S',
    ]
    if date_str is None:
        return date_str
    for format in formats:
        try:
            return datetime.strptime(date_str, format)
        except ValueError:
            pass
    raise InvalidTaskDueDateException()

def parse_int(value):
    try:
        return int(value)
    except ValueError:
        pass


def serialize(tasks):
    result = []
    for task in tasks:
        new_task = task.copy()
        new_task['due_on'] = task['due_on'].strftime('%Y-%m-%d %H:%M:%S')
        result.append(new_task)
    return result


def unserialize(blob):
    pass


def summary(tasks):
    result = {
        'total' : len(tasks),
        'pending' : 0,
        'done' : 0
    }
    count = 0
    for task in tasks:
        if task['status'] == 'pending':
            result['pending'] += 1
        elif task['status'] == 'done':
            result['done'] += 1
    return result
