class Solution(object):
    #set
    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set([])
        for ele in nums1:
            if ele in nums2:
                res.add(ele)
        return list(res)
    
    #two pointers
    def intersection2(self, nums1, nums2):
        nums1, nums2, res = sorted(nums1), sorted(nums2), []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            while p1 + 1 < len(nums1) and nums1[p1 + 1] == nums1[p1]:
                p1 += 1
            while p2 + 1 < len(nums2) and nums2[p2 + 1] == nums2[p2]:
                p2 += 1

            if nums1[p1] == nums2[p2]:
                res += [nums1[p1]]
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res
    
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
                
