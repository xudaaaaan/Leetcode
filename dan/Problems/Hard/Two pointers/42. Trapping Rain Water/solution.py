class Solution:
    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)
        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i + 1])
        res = 0
        for k in range(len(height)):
            res += max(0, min(leftmax[k], rightmax[k]) - height[k])
        return res
    
    def trap(self, height):
        left, right = 0, len(height) - 1
        lm, rm = 0, 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > lm:
                    lm = height[left]
                else:
                    res += (lm - height[left])
                left += 1
            else:
                if height[right] > rm:
                    rm = height[right]
                else:
                    res += (rm - height[right])
                right -= 1
        return res


