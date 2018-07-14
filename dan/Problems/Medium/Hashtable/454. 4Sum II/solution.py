class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic, res = {}, 0
        for a in A:
            for b in B:
                if (a + b) not in dic:
                    dic[a + b] = 1
                else:
                    dic[a + b] += 1
        for c in C:
            for d in D:
                if -(c + d) in dic:
                    res += dic[-(c + d)]
        return res
        
