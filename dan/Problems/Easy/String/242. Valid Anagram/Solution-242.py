class Solution(object):
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        word1, word2 = [_ for _ in range(26)], [_ for _ in range(26)]
        for let in s:
            word1[letters.index(let)] += 1
        for let in t:
            word2[letters.index(let)] += 1
        return word1 == word2
    
    def isAnagram2(self, s, t):
        dic1, dic2 = {}, {}
        for ele in s:
            dic1.get(ele, 0) + 1
        for ele in t:
            dic2.get(ele, 0) + 1
        return dic1 == dic2
        
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
        
        
