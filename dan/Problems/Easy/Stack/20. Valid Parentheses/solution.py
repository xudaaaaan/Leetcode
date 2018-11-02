class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = set(["[", "{", "("])
        right = set(["]", "}", ")"])
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            elif i in right and stack:
                match = stack.pop()
                if match + i not in ["[]", "{}", "()"]:
                    return False
            else:
                return False
        return True if not stack else False
                
        
