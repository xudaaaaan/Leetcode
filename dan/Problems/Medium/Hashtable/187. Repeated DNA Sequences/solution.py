from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        dic, res = defaultdict(int), []
        for i in range(0, len(s) - 9):
            seq = s[i:(i+10)]
            if dic[seq] == 1:
                res.append(seq)
            dic[seq] += 1
        return res
        
