class Solution(object):
    #Recursive
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
        if (root.left and not root.right) or (root.right and not root.left):
            return False
        
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and node2 and node1.val == node2.val:
                return (helper(node1.left, node2.right) and helper(node1.right, node2.left))
            else:
                return False
            
        return helper(root.left, root.right)
    
    #Iterative
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right):
            return True
        if (root.left and not root.right) or (root.right and not root.left):
            return False
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif node1 and node2 and node1.val == node2.val:
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))

            else:
                return False
        return True
    
        
