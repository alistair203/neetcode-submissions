class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryover = 1
        for i in reversed(range(len(digits))):
            newdigit = digits[i] + carryover
            if newdigit == 10:
                digits[i] = 0
            else:
                carryover = 0
                digits[i] = newdigit
        if carryover == 1:
            digits = [1] + digits
        return digits

        