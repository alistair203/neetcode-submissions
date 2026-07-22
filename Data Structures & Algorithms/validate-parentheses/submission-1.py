class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_mapping = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif stack and close_open_mapping[c] == stack[-1]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True