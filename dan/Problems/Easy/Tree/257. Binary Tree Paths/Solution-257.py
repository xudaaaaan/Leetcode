# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution(object):
    #dfs + stack
    def binaryTreePaths1(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
        return res
    
    #bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.left:
                queue.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                queue.append((node.right, ls + str(node.val) + "->"))
        return res
    
    #recursion
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.helper(root, "", res)
        return res
        
    def helper(self, node, ls, res):
        if not node.left and not node.right:
            res.append(ls + str(node.val))
        if node.left:
            self.helper(node.left, ls + str(node.val) + "->", res)
        if node.right:
            self.helper(node.right, ls + str(node.val) + "->", res)


