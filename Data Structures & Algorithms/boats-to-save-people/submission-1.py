class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        res = 0
        while people:
            if people[-1] + people[0] <= limit and len(people) > 1:
                people.pop()
                people.pop(0)
            else:
                people.pop()
            res += 1
        return res