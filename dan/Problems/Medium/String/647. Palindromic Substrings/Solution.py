class Solution:
    # Brute solution
    def countSubstrings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j] and s[i:j+1] == s[i:j+1][::-1]:
                    res += 1
        return res
    
    def countSubstrings2(self, s):
        if s == "":
            return 0
        res = 0
        for center in range(2 * len(s) - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res
    
    # Manacher's algorithm
    def countSubstrings(self, s):
        A = "$#" + "#".join(s) + "#%"
        Z = [0] * len(A)
        right, center = 0, 0
        for i in range(1, len(A) - 1):
            if i < right:
                Z[i] = min(Z[2 * center - i], right - i)
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if Z[i] + i > right:
                right = Z[i] + i
                center = i
        return sum([(v + 1) // 2 for v in Z])
            
