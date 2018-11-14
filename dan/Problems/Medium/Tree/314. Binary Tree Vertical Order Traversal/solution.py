# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from collections import deque
class Solution(object):
    def verticalOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        dic = defaultdict(list)
        q = deque()
        q.append((root, 0))
        while q:
            node, c = q.popleft()
            if node:
                dic[c].append(node.val)
                q.append((node.left, c + 1))
                q.append((node.right, c - 1))
                
        return zip(*sorted(dic.items(), key = lambda x: x[0], reverse = True))[1]
    
    def verticalOrder(self, root):
        if not root:
            return []
        dic = defaultdict(list)
        q = [(root, 0)]
        for node, c in q:
            if node:
                dic[c].append(node.val)
                q += [(node.left, c + 1), (node.right, c - 1)]
        return zip(*sorted(dic.items(), key = lambda x: x[0], reverse = True))[1]
