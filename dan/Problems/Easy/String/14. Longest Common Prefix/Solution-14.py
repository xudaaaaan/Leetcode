class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        strs = sorted(strs)
        f, l, i= strs[0], strs[-1], 0
        while i < min(len(f), len(l)):
            if f[i] == l[i]:
                i += 1
            else:
                break
        return f[:i] if i > 0 else ""
    
    def LCP(self, str1, str2):
        i = 0
        while i < min(len(str1), len(str2)):
            if not str1[i] == str2[i]:
                break
            i += 1
        return str1[:i] if i > 0 else ""
            
                     
    def longestCommonPrefix2(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        return reduce(self.LCP, strs)
