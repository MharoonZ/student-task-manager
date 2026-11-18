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
        task = Task(self._next_id, title)
        self._tasks[task.identifier] = task
        self._next_id += 1
        return task

    def display(self):
        return tuple(self._tasks.values())
