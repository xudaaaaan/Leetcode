class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([i for i in s.split(" ") if not i.strip() == ""][::-1])
        
