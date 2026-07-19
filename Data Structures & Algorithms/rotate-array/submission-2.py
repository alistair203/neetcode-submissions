class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        moved_count = 0
        i = 0
        n = len(nums)
        k = k % n
        while moved_count < n:
            j = i
            to_move = nums[j]
            while True:
                j = (j + k) % n
                temp = nums[j]
                nums[j] = to_move
                to_move = temp
                moved_count += 1
                if j == i:
                    i += 1
                    break



        