class Solution:
    def rotateString1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) in [0,1]:
            return A == B
        for _ in range(len(A)):
            A = A[1:] + A[0]
            if A == B:
                return True
        return False
    
    def rotateString(self, A, B):
        return B in A + A if len(A) == len(B) else False

        
