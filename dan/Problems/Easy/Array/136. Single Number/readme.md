# Problem 136
[Link](https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.)

# Trick:
XOR operation:
a ^ b = b ^ a   
a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c  
d = a ^ b ^ c ----->>>>  a = d ^ b ^ c   
a ^ b ^ a = b
0 ^ 0 = 0
