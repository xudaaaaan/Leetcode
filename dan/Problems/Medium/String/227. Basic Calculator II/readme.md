# Problem 227
[Link](https://leetcode.com/problems/basic-calculator-ii/description/)

# Trick
Store the last number and last sign; When the current char is an operation or the last char, calculate the last number, which depend on what last sign is. If the last sign is + or -, just append the number to the stack; If "*" or "/", pop the stack, and calculate the poped element and the current number, then append the result to the stack.
