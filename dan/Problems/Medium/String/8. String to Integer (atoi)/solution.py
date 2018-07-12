class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res, flag = "", 0
        for i in str:
            if flag == 1 and not i.isdigit():
                break
            if flag == 0 and i != " " and not (i.isdigit() or i == "-" or i == "+"):
                break
            if flag == 0 and (i.isdigit() or i == "-" or i == "+"):
                flag = 1
                res += i
            elif flag == 1 and i.isdigit():
                res += i
                
        if not flag or (len(res) == 1 and res[0] in ["+", "-"]):
            return 0
        elif int(res) > 2**31 - 1:
            return 2**31 - 1
        elif int(res) < -2**31:
            return -2**31
        else:
            return int(res)
        
