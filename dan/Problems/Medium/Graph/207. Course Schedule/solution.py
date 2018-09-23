class Solution(object):
    #DFS. Using stack.
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        stack, arc_num, cnt = [], len(prerequisites), 0
        
        #Initialize the graph
        graph = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        
        #Add edges to the graph
        for pair in prerequisites:
            pre, lat = pair[1], pair[0]
            graph[pre].append(lat)
            indegree[lat] += 1
            
        #Initialize the stack
        for idx, ind in enumerate(indegree):
            if ind == 0:
                stack.append(idx)
                
        while stack:
            course = stack.pop()
            cnt += 1
            for lat in graph[course]:
                indegree[lat] -= 1
                if indegree[lat] == 0:
                    stack.append(lat)
                    
        return cnt == numCourses
            
        
        
