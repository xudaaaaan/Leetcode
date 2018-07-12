class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i, char in enumerate(input):
            if char in "+-*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                res += [self.ops(char, x, y) for x in res1 for y in res2]
        return res
    
    def ops(self, op, x, y):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        else:
            return x * y
        


