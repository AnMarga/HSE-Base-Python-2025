import sys
from dataclasses import dataclass, field
from typing import Callable

TASK_REGISTRY = {}

@dataclass
class Task:
    task_func: Callable
    description: str = None
    cpu: int = None
    memory: int = None
    name: str = field(init=False)

    def __post_init__(self):
        self.name = self.task_func.__name__

    def register(self):
        TASK_REGISTRY[self.name] = self

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nCPU: {self.cpu}\nMemory: {self.memory}"

def task(description=None, cpu=None, memory=None):
    def decorator(func):
        t = Task(task_func=func, description=description, cpu=cpu, memory=memory)
        t.register()
        return func
    return decorator

exec(sys.stdin.read())
