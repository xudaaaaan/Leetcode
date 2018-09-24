class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seen = set()
        ans = []
        def dfs(node):
            for i in map(str, range(k)):
                pos = node + i
                if not pos in seen:
                    seen.add(pos)
                    dfs(pos[1:])
                    ans.append(i)
        dfs("0" * (n - 1))
        return "".join(ans) + "0" * (n - 1)
        
