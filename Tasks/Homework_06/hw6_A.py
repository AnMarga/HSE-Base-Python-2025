import sys

class LittleBell:
    def sound(self):
        print("ding")

class BigBell:
    def __init__(self):
        self.flag = True
        
    def sound(self):
        if self.flag:
            print("ding")
        else:
            print("dong")
        self.flag = not self.flag

class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)
        
    def append(self, bell):
        self.bells.append(bell)
        
    def sound(self):
        for bell in self.bells:
            bell.sound()
        print("...")

exec(sys.stdin.read())
