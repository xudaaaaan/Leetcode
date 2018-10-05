class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return None
        begin, end = 0, m
        while begin <= end:
            i = begin + (end - begin) / 2
            j = (m + n) / 2 - i
            if(i > 0 and nums1[i - 1] > nums2[j]):
                end = i
            elif(i < m and nums2[j - 1] > nums1[i]):
                begin = i + 1
            else:
                break
        if i == 0:
            maxleft = nums2[j - 1]
        elif j == 0:
            maxleft = nums1[i - 1]
        else:
            maxleft = max(nums1[i - 1], nums2[j - 1])
            
        if j == n:
            minright = nums1[i]
        elif i == m:
            minright = nums2[j]
        else:
            minright = min(nums1[i], nums2[j])
            
        if (m + n) % 2 == 0:
            return (maxleft + minright) / 2.0
        else:
            return minright
        
        
