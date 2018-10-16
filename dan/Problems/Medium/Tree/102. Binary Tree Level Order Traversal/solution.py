# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([(1, root)])
        res = [[]]
        tag = 1
        while queue:
            n, node = queue.popleft()
            if n >= tag * 2:
                tag = n
                res.append([])
            res[-1].append(node.val)
            if node.left:
                queue.append((n * 2, node.left))
            if node.right:
                queue.append((n * 2 + 1, node.right))
             
        return res 
            
            
        
    
        
        
