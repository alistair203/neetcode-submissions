class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackmin or val <= self.stackmin[-1]:
            self.stackmin.append(val)

    def pop(self) -> None:
        res = self.stack.pop()
        if self.stackmin[-1] == res:
            self.stackmin.pop()
        return res

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]
        
