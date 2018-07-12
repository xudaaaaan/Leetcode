class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        isPositive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
       
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= (temp << 1):
                temp = temp << 1
                i = i << 1
            dividend -= temp
            res += i
        if not isPositive:
            res = -res
        if (res > 2**31-1) or (res < -2**31):
            return 2 ** 31 - 1
        else:
            return res
            
            
