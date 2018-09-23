#[Problem 207](https://leetcode.com/problems/course-schedule/description/)
##Trick
It is a classic problem in graph: topological sort. The general way is to first find all nodes that have zero indegrees, and put them in a queue(BFS) or stack(DFS). Then pull out a node from the queue, remove its relations to other nodes and make the indegree of all nodes that it points to minus one. If new nodes that have zero indegree appear, add them to the queue. Repeat this until the queue isempty. 
