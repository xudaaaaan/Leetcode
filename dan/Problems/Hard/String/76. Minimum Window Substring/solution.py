import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt_t = collections.Counter(t)
        cnt_s = collections.defaultdict(int)
        n_t = len(cnt_t)
        n_s = 0
        l, r = 0, 0
        res = []
        while r < len(s):
            if s[r] in cnt_t:
                cnt_s[s[r]] += 1
                if cnt_s[s[r]] == cnt_t[s[r]]:
                    n_s += 1
            if n_s == n_t:
                while l <= r and n_s == n_t:
                    l += 1
                    cnt_s[s[l - 1]] -= 1
                    if s[l - 1] in cnt_t and cnt_s[s[l - 1]]  < cnt_t[s[l - 1]]:
                        n_s -= 1
                        if not res or res[1] - res[0] > r - l + 1:
                            res = [l- 1, r]
                        break
                    
            r += 1
        return s[res[0] : (res[1] + 1)] if res else ""
        
        
