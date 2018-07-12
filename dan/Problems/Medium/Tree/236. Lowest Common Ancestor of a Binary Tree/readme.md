# Problem 236
[Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

# Trick
1 Use recursion  
2 Use stack to traverse the tree and record the parent of each node by a dictionary; Then backtrack from the two nodes, when one node become root, change it to another target.(3 + 2 = 2 + 3)  
