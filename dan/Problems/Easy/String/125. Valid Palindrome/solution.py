class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = [char.lower() for char in s if char.isalnum()]
        return c == c[::-1]
       
