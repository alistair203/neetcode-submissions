class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        positions = set(position)
        pos_speed = dict(zip(position, speed))
        j = 0
        for i in range(target):
            if i in positions:
                position[j] = i
                speed[j] = pos_speed[i]
                j += 1
        fleet_times = []
        res = 0
        for i in range(n):
            time = (target - position[n - 1 - i]) / speed[n - 1 - i]
            if fleet_times and fleet_times[-1] >= time:
                continue
            else:
                fleet_times.append(time)
                res += 1
        return res
        

        