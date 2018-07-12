import collections

class Solution:
    def customSortString1(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic = {}
        for i in range(len(S)):
            dic[S[i]] = i
        T = sorted(T, key = lambda x: dic.get(x, len(S)))
        res = ""
        for e in T:
            res += e
        return res
    
    def customSortString(self, S, T):
        C = collections.Counter(T)
        res = ""
        for ele in S:
            res += C[ele] * ele
            del C[ele]
        for char, times in C.items():
            res += char * times
        return res
        
        
