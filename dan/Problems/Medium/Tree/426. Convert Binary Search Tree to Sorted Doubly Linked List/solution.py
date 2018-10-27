"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList1(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
            
        else:
            l = self.treeToDoublyList(root.left)
            r = self.treeToDoublyList(root.right)
            l_cur, r_cur = l, r
            if l:
                while l_cur.right and (not l_cur.right == l):
                    l_cur = l_cur.right
                l_cur.right = root
                root.left = l_cur
                h = l
            else:
                h = root
            if r:
                while r_cur.right and (not r_cur.right == r):
                    r_cur = r_cur.right
                root.right = r
                r.left = root
                t = r_cur
            else:
                t = root
   
            t.right = h
            h.left = t
            return h
        
    def treeToDoublyList(self, root):
        if not root: return
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right        
            
