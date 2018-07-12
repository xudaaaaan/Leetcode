class Solution:
    def majorityElement1(self, nums):
        
        """:type nums: List[int]
        :rtype: int"""
        
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2 and not nums[0] == nums[1]:
            return 'Error'
        
        m1 = self.majorityElement(nums[:l//2])
        m2 = self.majorityElement(nums[l//2:])
        if m1 == "Error" and m2 == "Error":
            return "Error"
        elif m1 == "Error" and not m2 == "Error":
            cnt = 0
            for ele in nums:
                if ele == m2:
                    cnt += 1
            return m2 if cnt >= l / 2 else "Error"
               
        elif not m1 == "Error" and m2 == "Error":
            cnt = 0
            for ele in nums:
                if ele == m1:
                    cnt += 1
            return m1 if cnt >= l / 2 else "Error"
               
        elif m1 == m2:
            return m1
        else:
            cnt1, cnt2 = 0, 0
            for ele in nums:
                if ele == m1:
                    cnt1 += 1
                if ele == m2:
                    cnt2 += 1
            if cnt1 > cnt2:
                return m1
            elif cnt1 < cnt2:
                return m2
            else:
                return "Error"

    def majorityElement2(self, nums):
        return sorted(nums)[len(nums)//2]
    
    def majorityElement(self, nums):
        dic = {}
        for ele in nums:
            if not ele in dic:
                dic[ele] = 1
            if dic[ele] > len(nums) / 2:
                return ele
            else:
                dic[ele] += 1
    

            
            