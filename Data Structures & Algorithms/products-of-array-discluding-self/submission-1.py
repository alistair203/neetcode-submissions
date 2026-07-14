class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = []
        prod = 1
        for i in range(n):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zeros.append(i)
        output = [0] * n
        if len(zeros) > 1:
            return output
        elif len(zeros) == 1:
            output[zeros[0]] = prod
            return output
        else:
            for i in range(n):
                output[i] = prod // nums[i]
            return output


        