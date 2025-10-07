import sys

class Student:
    def __init__(self, email: str, full_name: str) -> None:
        self.email = email
        self.full_name = full_name
        self._marks = {"hw": [], "test": [], "exam": []}
        self._sums = {"hw": 0, "test": 0, "exam": 0}

    def put_mark(self, mark: int, kind: str = "hw") -> None:
        self._marks[kind].append(mark)
        self._sums[kind] += mark

    def change_mark(self, num: int, mark: int, kind: str = "hw") -> None:
        self._sums[kind] += mark - self._marks[kind][num]
        self._marks[kind][num] = mark

    def get_result(self, ndigits: int = 2) -> float:
        total = 0.0
        weights = {"hw": 0.3, "test": 0.3, "exam": 0.4}
        has_marks = False
        for kind in ["hw", "test", "exam"]:
            count = len(self._marks[kind])
            if count > 0:
                has_marks = True
                total += (self._sums[kind] / count) * weights[kind]
        return round(total, ndigits) if has_marks else 0

    def marks_count(self, kind: str = "hw") -> int:
        return len(self._marks[kind])

    def __str__(self) -> str:
        return f"{self.email} {self.full_name}"

exec(sys.stdin.read())
