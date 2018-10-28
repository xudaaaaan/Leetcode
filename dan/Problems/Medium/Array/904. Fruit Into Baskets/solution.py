class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        longest, cur, s = 0, 0, set()
        for i in range(len(tree)):
            if tree[i] in s:
                cur += 1
            else:
                if len(s) < 2:
                    s.add(tree[i])
                    cur += 1
                else:
                    longest = max(longest, cur)
                    j = i - 1
                    s = set([tree[i], tree[j]])
                    while j > 0 and tree[j] == tree[j - 1]:
                        j -=1  
                    cur = i - j + 1
        return max(longest, cur)
            
        
