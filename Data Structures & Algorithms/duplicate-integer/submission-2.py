class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_no_dupes = set()
        for num in nums:
            if num in nums_no_dupes:
                return True
            nums_no_dupes.add(num)
        return False
