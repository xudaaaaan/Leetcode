class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        l = [2, 3, 5]
        while not num == 1:
            ori = num
            for ele in l:
                if num % ele == 0:
                    num /= ele
            if num == ori:
                break
        return num == 1
