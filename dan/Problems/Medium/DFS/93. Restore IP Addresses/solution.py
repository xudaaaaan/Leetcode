class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12 or len(s) < 4:
            return []
        
        res = []
        def helper(s, cur, k):
            if k == 3 and s and 0 <= int(s) < 256 and str(int(s)) == s:
                cur.append(s)
                res.append(".".join(cur))
            else:
                for i in range(len(s)):
                    if i == 3:
                        break
                    t = s[:i+1]
                    if 0 <= int(t) < 256 and str(int(t)) == t:
                        helper(s[i+1:], cur + [t], k + 1)
        helper(s, [], 0)
        return res
