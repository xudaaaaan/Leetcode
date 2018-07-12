class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, letters, l = 0, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", len(s) - 1
        for char in s:
            num += (26 ** l) * (letters.index(char) + 1)
            l -= 1
        return num
        
        
