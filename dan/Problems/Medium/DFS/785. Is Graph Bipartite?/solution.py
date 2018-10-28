class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        cla = [0 for i in range(len(graph))]
        cla[0] = 1
        stack = [0]
        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if cla[nei] == cla[node]:
                    return False
                elif not cla[nei]:
                    stack.append(nei)
                    cla[nei] = -cla[node]
            if not stack:
                for i in range(len(cla)):
                    if cla[i] == 0:
                        stack.append(i)
                        cla[i] = 1
                        break
                        
        return True
