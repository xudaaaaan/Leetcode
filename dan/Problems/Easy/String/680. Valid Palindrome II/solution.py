class Solution:
    def validPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.s = s
        def helper(i, j, n):
            if i >= j:
                return True
            if self.s[i] == self.s[j]:
                while i < j and self.s[i] == self.s[j]:
                    i += 1
                    j -= 1
                return helper(i, j, n)
            
            else:
                if n == 0:
                    return False
                else:
                    return helper(i + 1, j, 0) or helper(i, j - 1, 0)
        return helper(0, len(self.s) - 1, 1)
    
    def validPalindrome(self, s):
        def isPali(i, j):
            for k in range((j - i + 1)//2):
                if not s[i] == s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for i in range(len(s) // 2):
            if not s[i] == s[-i - 1]:
                return isPali(i + 1, len(s) - 1 - i) or isPali(i, len(s) - 2 - i)
        return True
