from collections import deque
class MyStack:

    def __init__(self):
        self.main_q = deque()

    def push(self, x: int) -> None:
        helper_q = deque([x])
        while self.main_q:
            helper_q.appendleft(self.main_q.pop())
        self.main_q = helper_q


    def pop(self) -> int:
        return self.main_q.pop()
        

    def top(self) -> int:
        return self.main_q[-1]


    def empty(self) -> bool:
        if self.main_q:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()