class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res, i = "", len(S) - 1
        while i >= 0:
            cnt = 0
            while cnt < K and i >= 0:
                char = S[i]
                if char != "-":
                    res += char.upper()
                    cnt += 1
                i -= 1
            if cnt == K:
                res += "-"
        if not res:
            return res
        else:
            return res[::-1] if res[-1] != "-" else res[::-1][1:]
        
            
        
