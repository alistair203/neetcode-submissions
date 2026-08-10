class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {}
        for prereq in prerequisites:
            reqs.setdefault(prereq[0], []).append(prereq[1])
        safe = set()
        for i in range(numCourses):
            stack = [(i, False)]
            path = set()
            while stack:
                course, checked_neighbours = stack.pop()
                if course not in reqs or course in safe:
                    continue
                if checked_neighbours:
                    safe.add(course)
                    path.remove(course)
                elif course in path:
                    return False
                else:
                    path.add(course)
                    stack.append((course, True))
                    for req in reqs[course]:
                        stack.append((req, False))
        return True
                



        