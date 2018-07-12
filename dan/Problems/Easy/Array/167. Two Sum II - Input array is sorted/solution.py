class Solution:
    #Using dictionary
    def twoSum1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(numbers)):
            if dic.get(numbers[i], False):
                return [dic[numbers[i]], i + 1]
            dic.setdefault(target - numbers[i], i + 1)
            
    #Using two pointers   
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < len(numbers) and right > 0:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
            
