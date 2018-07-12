import functools
class Solution:
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for ele in nums:
            x = a.get(ele, 0)
            if x == 0:
                a[ele] = 1
            else:
                a.pop(ele)
        return list(a.items())[0][0]
    
    def singleNumber(self, nums):
        return functools.reduce(lambda x, y: x ^ y, nums)
    
    
        
                

                
