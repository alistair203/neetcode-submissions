class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        total_error = sum([abs(a - x) for a in arr[0:k]])
        current_arr = arr[0:k]
        for l in range(len(arr) - k):
            r = l + k
            prev_error = total_error
            total_error -= abs(x - arr[l])
            total_error += abs(x - arr[r])
            if total_error > prev_error:
                return current_arr
            elif total_error == prev_error:
                continue
            else:
                current_arr = arr[l + 1: r + 1]
        return current_arr
        