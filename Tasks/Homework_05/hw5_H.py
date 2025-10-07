import sys

class Student:
    def __init__(self, email: str, full_name: str) -> None:
        self.email = email
        self.full_name = full_name
        self.marks: list[int] = []

    def put_mark(self, mark: int) -> None:
        self.marks.append(mark)

    def change_mark(self, num: int, new_mark: int) -> None:
        self.marks[num] = new_mark

    def get_result(self) -> float:
        if not self.marks:
            return 0
        return round(sum(self.marks) / len(self.marks), 2)

    def __len__(self) -> int:
        return len(self.marks)

    def __str__(self) -> str:
        return f"{self.email} {self.full_name}"

exec(sys.stdin.read())
