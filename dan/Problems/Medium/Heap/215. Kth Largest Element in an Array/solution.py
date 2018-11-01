import heapq
class Solution:
    # Max heap
    # Time complexity: O(n + klogn) Space: O(n)
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = nums[0]
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
    
    # Min heap
    # Time complexity: O(n + (n - k)logk) Space complexity: O(k)
    def findKthLargest(self, nums, k):
        h = [-float("inf")] * k
        heapq.heapify(h)
        for n in nums:
            if n > h[0]:
                heapq.heappushpop(h, n)
        return h[0]
            
            
        
