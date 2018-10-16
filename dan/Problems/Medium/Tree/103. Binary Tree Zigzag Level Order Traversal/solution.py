# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack1 = [(1, root)]
        stack2 = []
        res = [[]]
        tag = 1 
        while stack1 or stack2:
            while stack1:
                n, node = stack1.pop()
                if n >= tag * 2:
                    tag *= 2
                    res.append([])
                res[-1].append(node.val)
                if node.left:
                    stack2.append((n * 2, node.left))
                if node.right:
                    stack2.append((n * 2 + 1, node.right))
            while stack2:
                n, node = stack2.pop()
                if n >= tag * 2:
                    tag *= 2
                    res.append([])
                res[-1].append(node.val)
                if node.right:
                    stack1.append((n * 2 + 1, node.right))        
                if node.left:
                    stack1.append((n * 2, node.left))
        return res
