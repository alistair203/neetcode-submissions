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
        l, r = 0, len(people) - 1
        while l <= r:
            person1 = people[r]
            r -= 1
            res += 1
            if person1 + people[l] <= limit:
                l += 1
        return res