# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Slow approuch
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        objs, stack, res = [p, q],  [[root]], []
        while stack:
            node = stack.pop()
            if node[-1] in objs:
                res.append(node)
                objs.remove(node[-1])
            if not objs:
                break
            if node[-1].right:
                stack.append(node + [node[-1].right])
            if node[-1].left:
                stack.append(node + [node[-1].left])
        i = 0
        while i < min(len(res[0]), len(res[1])):
            if res[0][i] == res[1][i]:
                i += 1
            else:
                return res[0][i - 1]
        return res[0][i - 1]
    
    # Recursion
    def lowestCommonAncestor2(self, root, p, q):
        if root in [None, p, q]:
            return root
        left, right = [self.lowestCommonAncestor(node, p, q) for node in [root.left, root.right]]
        return root if left and right else max(left, right)
    
    # Smart way to search common ancestor
    def lowestCommonAncestor(self, root, p, q):
        stack, dic = [root], {}
        while stack:
            node = stack.pop()
            if node.right:
                dic[node.right] = node
                stack.append(node.right)
            if node.left:
                dic[node.left] = node
                stack.append(node.left)
        node1, node2 = p, q
        while node1 != node2:
            node1 = dic[node1] if node1 != root else q
            node2 = dic[node2] if node2 != root else p
        return node1
        
                
        
        
