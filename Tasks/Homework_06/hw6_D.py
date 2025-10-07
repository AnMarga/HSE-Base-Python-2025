import sys

class ExtendedList(list):
    @property
    def reversed(self):
        return list(reversed(self))

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, value):
        self[0] = value

    @property
    def last(self):
        return self[-1]

    @last.setter
    def last(self, value):
        self[-1] = value

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, value):
        current = len(self)
        if value > current:
            self.extend([None] * (value - current))
        elif value < current:
            del self[value:]

exec(sys.stdin.read())
