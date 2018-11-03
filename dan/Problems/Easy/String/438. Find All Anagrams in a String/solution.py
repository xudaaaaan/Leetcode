from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        res = []
        pc = Counter(p)
        sc = Counter(s[:len(p) - 1])
        
        for i in range(len(p) - 1, len(s)):
            sc[s[i]] += 1
            if sc == pc:
                res.append(i-len(p)+1)
            sc[s[i-len(p)+1]] -= 1
            if sc[s[i-len(p)+1]] == 0:
                sc.pop(s[i-len(p)+1])
        return res
