class TimeMap:

    def __init__(self):
        self.maps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.maps:
            self.maps[key].append((timestamp, value))
        else:
            self.maps[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maps:
            return ""
        values = self.maps[key]
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][0] == timestamp:
                return values[m][1]
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

