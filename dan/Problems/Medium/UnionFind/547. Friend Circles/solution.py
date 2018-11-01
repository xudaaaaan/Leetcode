class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(k):
            if not k == parent[k]:
                parent[k] = find(parent[k])
            return parent[k]
        
        def merge(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            else:
                parent[root_j] = root_i
                if rank[root_i] == rank[root_j]:
                    rank[root_i] += 1
            return
            
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j]:
                    merge(i, j)
                    
        return sum(idx == ele for idx, ele in enumerate(parent))
                   
       
