class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        def add_to_stack(a):
            if stack and (stack[-1] > 0 and a < 0):
                b = stack.pop()
                if abs(b) > abs(a):
                    add_to_stack(b)
                elif abs(a) > abs(b):
                    add_to_stack(a)
            else:
                stack.append(a)
        for a in asteroids:
            add_to_stack(a)
        return stack

        