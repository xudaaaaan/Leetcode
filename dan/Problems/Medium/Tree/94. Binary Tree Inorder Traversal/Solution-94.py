# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #use recursion
    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right
    #use iteration
    def inorderTraversal(self, root):
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, node, result):
        if node == None:
            return 
        self.helper(node.left, result)
        result.append(node.val)
        self.helper(node.right, result)
            
    

            
