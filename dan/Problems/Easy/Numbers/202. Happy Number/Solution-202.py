class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set([])
        while not n == 1:
            n = list(map(int, str(n)))
            t = 0
            for ele in n:
                t += ele * ele
            n = t
            if n in s:
                return False
            s.add(n)
        return True


