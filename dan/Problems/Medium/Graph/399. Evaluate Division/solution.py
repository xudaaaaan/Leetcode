from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph, res = defaultdict(list), []
        for idx, pair in enumerate(equations):
            a, b, result = pair[0], pair[1], values[idx]
            graph[a].append((b, result))
            graph[b].append((a, 1.0/result))
            
        def dfs(x, y, s):
            if x == y and x in graph:
                return 1.0
            for tuples in graph[x]:
                node, result = tuples[0], tuples[1]
                if node in s:
                    continue
                s.add(node)
                ans = dfs(node, y, s)
                if not ans == -1.0:
                    return result * ans
            return -1.0
            
        for idx, pair in enumerate(queries):
            a, b = pair[0], pair[1]
            res.append(dfs(a, b, {a}))
        return res
            
            
        
