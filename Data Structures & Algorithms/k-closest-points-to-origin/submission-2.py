class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_distances = []
        heapq.heapify_max(closest_distances)
        for p in points:
            d = p[0]**2 + p[1]**2
            if len(closest_distances) == k:
                heapq.heappushpop_max(closest_distances, d)
            else:
                heapq.heappush_max(closest_distances, d)
        closest_distances = set(closest_distances)
        return [p for p in points if p[0]**2 + p[1]**2 in closest_distances]

        