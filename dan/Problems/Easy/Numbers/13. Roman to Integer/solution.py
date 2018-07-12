class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, res = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}, 0
        while len(s) > 0:
            if len(s) > 1 and s[:2] in dic:
                res += dic[s[:2]]
                s = s[2:]
            else:
                res += dic[s[0]]
                s = s[1:]
        return res
    
     
