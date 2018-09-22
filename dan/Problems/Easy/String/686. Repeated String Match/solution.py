class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a, rep = A, 1
        for i in range(1, len(B)/len(A) + 3):
            if B in a:
                return i
            a += A
        return -1
        
