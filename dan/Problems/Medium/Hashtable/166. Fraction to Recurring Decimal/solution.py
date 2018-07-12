import functools
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        is_positive = (numerator > 0) is (denominator > 0)
        numerator, denominator = abs(numerator), abs(denominator)
        unit, remainder = divmod(numerator, denominator)
        
        if remainder == 0:
            return str(unit) if is_positive else "-" + str(unit)
        
        res = [str(unit), "."]
        dic = {}
        while not remainder == 0:
            if remainder in dic:
                res.insert(dic[remainder],"(")
                res.append(")")
                break
            dic[remainder] = len(res)
            unit, remainder = divmod(remainder * 10, denominator)
            res.append(str(unit))
        res = functools.reduce(lambda x,y: x + y, res)
        
        return res if is_positive else "-" + res
