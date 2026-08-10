class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {}
        for prereq in prerequisites:
            reqs.setdefault(prereq[0], []).append(prereq[1])
        safe = set()
        visiting = set()
        def dfs(course):
            if course in safe or course not in reqs:
                return True
            if course in visiting:
                return False
            visiting.add(course)
            for req in reqs[course]:
                if not dfs(req):
                    return False
            visiting.remove(course)
            safe.add(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

