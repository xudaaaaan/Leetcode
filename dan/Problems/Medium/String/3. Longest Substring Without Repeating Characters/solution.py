class Solution:
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        lm = 0
        for i in range(len(s)):
            window = set([s[i]])
            l = 1
            for j in range(i + 1, len(s)):
                if not s[j] in window:
                    window.add(s[j])
                    l += 1
                else:
                    break
            lm = max(lm, l)
        return lm
    
    def lengthOfLongestSubstring(self, s):
        usedChar, start, l= {}, 0, 0, 
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                l = max(l, i - start + 1)
            usedChar[s[i]] = i
        return l
                
   
