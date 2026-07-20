class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        counts = [0] * (m + 1)
        for p in people:
            counts[p] += 1
        j = 0
        for i in range(len(people)):
            while counts[j] == 0:
                j += 1
            people[i] = j
            counts[j] -= 1
        res = 0
        while people:
            if people[-1] + people[0] <= limit and len(people) > 1:
                people.pop()
                people.pop(0)
            else:
                people.pop()
            res += 1
        return res