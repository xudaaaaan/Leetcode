from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            if int(x + y) > int(y + x):
                return -1
            else:
                return 1
        nums = sorted(list(map(str, nums)), key = cmp_to_key(compare))
        res = "".join(nums)
        return res if int(res) != 0 else "0"
