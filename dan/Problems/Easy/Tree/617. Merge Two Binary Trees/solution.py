import collections
class Solution:
    #recursive
    def mergeTrees1(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left, t1.right = self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right)
        return t1 if t1 else t2
    #BFS + queue
    def mergeTrees(self, t1, t2):
        if not (t1 and t2):
            return t1 or t2
        q1, q2 = collections.deque([t1]), collections.deque([t2])
        while q1 and q2:
            node1, node2 = q1.popleft(), q2.popleft()
            if node1 and node2:
                node1.val += node2.val
                if not node1.left and node2.left:
                    node1.left = TreeNode(0)
                if not node1.right and node2.right:
                    node1.right = TreeNode(0)
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
            
        return t1
                    
            
        


