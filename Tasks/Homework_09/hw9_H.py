import sys
import time
from functools import wraps

class Analiser:
    def __init__(self):
        self.students = set()
        self.timings = {}
        self.usages = {}
        self.unique_usages = {}

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            student = kwargs.get("student")
            if student:
                self.students.add(student)

            fname = func.__name__

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start

            # обновляем статистику
            self.timings[fname] = self.timings.get(fname, 0) + elapsed
            self.usages[fname] = self.usages.get(fname, 0) + 1
            if fname not in self.unique_usages:
                self.unique_usages[fname] = set()
            if student:
                self.unique_usages[fname].add(student)

            return result
        return wrapper

    def get_avg_timing(self, fn):
        name = fn.__name__
        if self.usages.get(name, 0) == 0:
            return 0
        return self.timings[name] / self.usages[name]

    def get_perc_usages(self, fn):
        name = fn.__name__
        if not self.students:
            return 0
        return len(self.unique_usages.get(name, set())) / len(self.students)

    def get_all_students(self):
        return len(self.students)

    def workload(self):
        return sum(self.usages.values())

    def get_all_timing(self):
        return sum(self.timings.values())

exec(sys.stdin.read())
