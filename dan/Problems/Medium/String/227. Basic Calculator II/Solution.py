class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign, stack, num = "+", [], 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in ["+", "-", "*", "/"] or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    temp = stack.pop()
                    if temp/num < 0 and temp % num != 0:
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp // num)
                sign, num = s[i], 0
        return sum(stack)
                
                    
    
