class Solution(object):
    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        for i in range(len(s)):
            if not dic1.get(s[i], False):
                dic1[s[i]] = t[i]
            elif not dic1[s[i]] == t[i]:
                return False
        for i in range(len(t)):
            if not dic2.get(t[i], False):
                dic2[t[i]] = s[i]
            elif not dic2[t[i]] == s[i]:
                return False
        return True
    def isIsomorphic2(self, s, t):
        dic1, dic2 = {}, {}
        for i, ele in enumerate(s):
            dic1[ele] = dic1.get(ele, []) + [i]
        for i, ele in enumerate(t):
            dic2[ele] = dic2.get(ele, []) + [i]
        return sorted(list(dic1.values())) == sorted(list(dic2.values()))
    
    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    def isIsomorphic(self, s, t):
        a, b = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if not a[ord(s[i])] == b[ord(t[i])]:
                return False
            a[ord(s[i])] = i+1
            b[ord(t[i])] = i+1
        return True
        
   
