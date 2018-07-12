# Problem 258
[Link](https://leetcode.com/problems/add-digits/description/)
# Trick:
## No loop and recursion
N = a[0] * 1 + a[1] * 10 + a[2] * 100.....  
M = a[0] + a[1] + a[2] + .....   
1 % 9 = 1  
10 % 9 = 1   
100 % 9 = 1   
N % 9 = (a[0] + (a[1] * 10) % 9 + (a[2] * 100) % 9 + ...) % 9
      = (a[0] + a[1] + a[2] + ...) % 9 = M % 9   
## loop
Notice that reduce function is removed in Python3
import functools
functools.reduce()
