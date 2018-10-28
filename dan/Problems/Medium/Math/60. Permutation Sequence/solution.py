class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ref = reduce(lambda x, y: x * y, [i for i in range(1, n + 1)])
        res = ""
        n = [i + 1 for i in range(n)]
        while len(n) >= 1:
            ref /= len(n)
            num = (k - 1) // ref
            res += str(n[num])
            n.pop(num)
            k -= num * ref
        return res
        
