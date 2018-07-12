class Solution:
    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        else:
            return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])