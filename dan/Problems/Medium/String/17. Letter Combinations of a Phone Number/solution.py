class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic, res = {"2":("a", "b", "c"), "3":("d", "e", "f"), "4":("g", "h", "i"), "5":("j", "k", "l"), "6":("m", "n", "o"), "7":("p", "q", "r", "s"), "8":("t", "u", "v"), "9":("w","x","y","z")}, []
        def helper(digits, temp, res):
            if not digits:
                return
            if len(digits) == 1:
                for char in dic[digits[0]]:
                    res.append(temp + char)
            else:
                for char in dic[digits[0]]:
                    helper(digits[1:], temp + char, res)
        helper(digits, "", res)
        return res
