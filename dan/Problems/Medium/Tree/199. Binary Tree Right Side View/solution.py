# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque([(1, root)])
        tag, last, res = 1, None, []
        while queue:
            n, node = queue.popleft()
            if n >= 2 * tag:
                res.append(last)
                tag *= 2
            last = node.val
            if node.left:
                queue.append((n * 2, node.left))
            if node.right:
                queue.append((n * 2 + 1, node.right))
        res.append(last)
        return res
            
        
