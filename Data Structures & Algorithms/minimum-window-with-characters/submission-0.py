class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, len(s) - 1]
        t_chars = set(c for c in t)
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        l, r = 0, 0
        window_count = {s[0]: 1}
        needed_count = len(t)
        if s[0] in t_chars:
            needed_count -= 1
        while l <= r and r < len(s):
            if needed_count == 0:
                if r - l < res[1] - res[0]:
                    res[0], res[1] = l, r
                window_count[s[l]] -= 1
                if s[l] in t_chars and window_count[s[l]] < t_count[s[l]]:
                    needed_count += 1
                l += 1
            else:
                r += 1
                if r < len(s):
                    window_count[s[r]] = window_count.get(s[r], 0) + 1
                    if s[r] in t_chars and window_count[s[r]] <= t_count[s[r]]:
                        needed_count -= 1
        if res[0] == -1:
            return ""
        else:
            return s[res[0]: res[1] + 1]

        