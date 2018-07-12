import collections
class Solution:
    def numJewelsInStones1(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        c,res = collections.Counter(S), 0
        for char in J:
            if char in c:
                res += c[char]
        return res
    
    def numJewelsInStones(self, J, S):
        return len([s for s in S if s in J])
        
        
