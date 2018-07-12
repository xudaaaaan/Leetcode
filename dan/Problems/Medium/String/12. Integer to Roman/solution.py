class Solution:
    def intToRoman1(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        digits = [num // 1000, num % 1000 // 100, num % 100 // 10, num % 10]
        for i, num in enumerate(digits):
            if not num:
                continue
            if i == 0:
                res += "M" * num
            elif i == 1:
                if num == 4:
                    res += "CD"
                elif num == 9:
                    res += "CM"
                elif num <= 3:
                    res += "C" * num
                else:
                    res += "D"
                    res += "C" * (num - 5)
            elif i == 2:
                if num == 4:
                    res += "XL"
                elif num == 9:
                    res += "XC"
                elif num <= 3:
                    res += "X" * num
                else:
                    res += "L"
                    res += "X" * (num - 5) 
            else:
                if num == 4:
                    res += "IV"
                elif num == 9:
                    res += "IX"
                elif num <= 3:
                    res += "I" * num
                else:
                    res += "V"
                    res += "I" * (num - 5)
        return res
    
    def intToRoman(self, num):  
        keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        dic = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        curindex, res = len(keys) - 1, ""
        while num > 0:
            n = 0
            while num >= keys[curindex]:
                num -= keys[curindex]
                n += 1
            res += dic[curindex] * n
            curindex -= 1
        return res
                
                
