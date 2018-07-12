class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        re = str(x)[::-1]
        while re[0] == '0' and len(re) > 1:
            re = re[1:]
        if re[-1] == '-':
            re = '-' + re[:-1]
        re = int(re)
        return 0 if x >= 2**31 or x < -2**31 or re >= 2**31 or re < -2**31 else re


        
