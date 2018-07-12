# Problem 543
[Link](https://leetcode.com/problems/diameter-of-binary-tree/description/)

# Trick
Each possible path can be seen as related to a node, where depth(node.left) + depth(node.right) = path.  
So we can use common dfs to traverse the tree and compute the depth of each node, while at the same time keep record of the "path" of that node. Finally, find the longest path.
