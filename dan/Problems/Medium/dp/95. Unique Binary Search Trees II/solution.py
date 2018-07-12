# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees1(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def generate(f, t):
            if f > t:
                return [None]
            elif f == t:
                return [TreeNode(f)]
            else:
                res = []
                for i in range(f, t + 1):
                    left = generate(f, i - 1)
                    right = generate(i + 1, t)
                    for l in left:
                        for r in right:
                            node = TreeNode(i)
                            node.left = l
                            node.right = r
                            res.append(node)
                return res
                
        return generate(1, n)


