# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    #Traverse the tree in-order until meet p
    def inorderSuccessor1(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = []
        if root.right:
            stack.append(root.right)
        stack.append(root)
        if root.left:
            stack.append(root.left)
        visited = collections.defaultdict(int)
        visited[root] = 1
        tag = 0
        while stack:
            node = stack.pop()
            if visited[node] == 0:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                visited[node] = 1
            elif tag == 1:
                return node
            elif node == p:
                tag = 1
        return None
    
    #Notice that this is a BST! Not a normal tree!
    def inorderSuccessor(self, root, p):
        suc = None
        while root:
            if root == p:
                if not root.right:
                    return suc
                node = root.right
                while node.left:
                    node = node.left
                return node
            elif root.val < p.val:
                root = root.right
            else:
                suc = root
                root = root.left
