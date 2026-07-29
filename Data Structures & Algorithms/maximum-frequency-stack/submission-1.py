class FreqStack:

    def __init__(self):
        self.stacks = []
        self.freqs = {}

    def push(self, val: int) -> None:
        self.freqs[val] = 1 + self.freqs.get(val, 0)
        if self.freqs[val] > len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[self.freqs[val] - 1].append(val)

    def pop(self) -> int:
        res = self.stacks[-1].pop()
        self.freqs[res] -= 1
        if self.stacks[-1] == []:
            self.stacks.pop()
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()