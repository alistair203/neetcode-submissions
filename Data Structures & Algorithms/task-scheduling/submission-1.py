class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord("A")] += 1
        heapq.heapify_max(counts)
        to_push = deque()
        to_fill = len(tasks)
        seq_idx = 0
        while to_fill:
            for _ in range(n + 1):
                if counts:
                    freq = heapq.heappop_max(counts)
                    if freq > 0:
                        if freq > 1:
                            to_push.appendleft(freq - 1)
                        to_fill -= 1
                if to_fill:
                    seq_idx += 1
            while to_push:
                heapq.heappush_max(counts, to_push.pop())
        return seq_idx + 1
        