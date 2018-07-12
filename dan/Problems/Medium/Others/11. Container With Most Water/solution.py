class Solution:
    #time exceed error
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        heights = sorted(list(zip(height, range(1, len(height) + 1))), key = lambda x : x[0])
        res = []
        for i in range(len(heights)):
            if i == len(heights) - 1:
                break
            c = list(zip(*heights[i+1:]))[1]
            max_d = max(map(lambda x: abs(x - heights[i][1]), c))
            res.append(heights[i][0] * max_d)
        return max(res)
    
    def maxArea(self, height):
        i, j, m = 0, len(height) - 1, 0
        while i < j:
            m = max(m, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m
            
    
        
