class Solution:
    from collections import deque
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        days = []
        res = [0] * n
        for i in range(n):
            if not days:
                days.append(i)
            else:
                while days and temperatures[i] > temperatures[days[-1]]:
                    res[days[-1]] = i - days[-1]
                    days.pop()
                days.append(i)
        return res
            
        