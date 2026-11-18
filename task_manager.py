from dataclasses import dataclass


@dataclass
class Task:
    identifier: int
    title: str
    completed: bool = False


class TaskManager:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add(self, title):
        title = title.strip()
        if not title:
            raise ValueError('Enter a non-blank title.')
        task = Task(self._next_id, title)
        self._tasks[task.identifier] = task
        self._next_id += 1
        return task

    def display(self):
        return tuple(self._tasks.values())

    def complete(self, identifier):
        task = self._tasks.get(identifier)
        if task is None:
            return False
        task.completed = True
        return True

    def delete(self, identifier):
        return self._tasks.pop(identifier, None) is not None
