class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        elif root.left:
            temp = root.right
            root.right = root.left
            root.left = None
            node = root.right
            self.flatten(node)
            while node and node.right:
                node = node.right
            node.right = temp
        self.flatten(root.right)
        return
        
