# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        else:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left, root.right = self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]) if mid < len(nums) - 1 else None
            return root
        
       
    
         
        
