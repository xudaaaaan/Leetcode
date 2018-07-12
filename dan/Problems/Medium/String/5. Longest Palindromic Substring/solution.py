class Solution:
    #Manacher's algorithm
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        t = "@#" + "#".join(s) + "#%"
        a = [0 for i in range(len(t))]
        rightmost, center = 0, 0
        for i in range(1, len(a) - 1):
          
            if i < rightmost:
                a[i] = min(a[2*center - i], rightmost - i)
            while t[i + a[i] + 1] == t[i - a[i] - 1]:
                a[i] += 1
            if a[i] + i > rightmost:
                center, rightmost = i, a[i] + i
            
        index = a.index(max(a))
        return t[(index - a[index]) : (index + a[index] + 1)][1::2]
    
