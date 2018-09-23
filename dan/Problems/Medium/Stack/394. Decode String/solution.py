class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        repstack, resstack, i, num, res = [], [""], 0, 0, ""
        while i < len(s):
            while s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
                if not s[i].isdigit():
                    repstack.append(num)
                    num = 0
            if s[i] == "[":
                resstack.append(res)
                res = ""
            elif s[i] == "]":
                res = resstack.pop() + repstack.pop() * res
            else:
                res += s[i]
            i += 1
        return res
                
            
