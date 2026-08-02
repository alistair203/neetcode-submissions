class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26
        for task in tasks:
            freqs[ord(task) - ord("A")] += 1
        maxf = max(freqs)
        freqs.remove(maxf)
        max_idle = n * (maxf - 1)
        for f in freqs:
            max_idle -= min(maxf - 1, f)
        return len(tasks) + max(max_idle, 0)
        