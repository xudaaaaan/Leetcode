class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 10:
                return digits
            digits[i] -= 10
            if i > 0:
                digits[i - 1] += 1
            else:
                return [1] + digits
            
