class Solution:
    def decodeString(self, s: str) -> str:
        digits = set(str(i) for i in range(10))
        i = 0
        stack = []
        for c in s:
            print(stack)
            if c in digits:
                if not (stack and stack[-1].isnumeric()):
                    stack.append(c)
                else:
                    stack.append(stack.pop() + c)
            elif c == "[":
                stack.append("")
            elif c == "]":
                strin = stack.pop()
                num = int(stack.pop())
                if stack:
                    stack.append(stack.pop() + num * strin)
                else:
                    stack.append(num * strin)
            else:
                if stack:
                    stack.append(stack.pop() + c)
                else:
                    stack.append(c)
        return stack[0]
        
        