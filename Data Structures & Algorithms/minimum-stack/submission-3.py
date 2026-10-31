class MinStack:

    def __init__(self):
        self.ls = []

    def push(self, val: int) -> None:
        if self.ls:
            self.ls.append((val,min(val,self.ls[-1][1])))
        else:
            self.ls.append((val,val))

    def pop(self) -> None:
        self.ls.pop()

    def top(self) -> int:
        return self.ls[-1][0]

    def getMin(self) -> int:
        return self.ls[-1][1]