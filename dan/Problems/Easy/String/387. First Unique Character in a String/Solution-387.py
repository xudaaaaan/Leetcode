class Solution:
    
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        times = [0 for _ in range(26)]
        order = [len(s) for _ in range(26)]
        for i in range(len(s)):
            times[ord(s[i]) - 97] += 1
            if times[ord(s[i]) - 97] == 1:
                order[ord(s[i]) - 97] = i
            else:
                order[ord(s[i]) - 97] = len(s)
        if min(order) == len(s):
            return -1

        return min(order)
    
    #faster solution:
    def firstUniqChar_faster(self, s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        indexs = [s.index(i) for i in letters if s.count(i) == 1]
        return min(indexs) if not len(indexs) == 0 else -1
        