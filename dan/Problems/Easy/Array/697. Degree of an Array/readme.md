# Problem 697
[Link](https://leetcode.com/problems/degree-of-an-array/description/)

# Trick
a = {}
a.setdefault('a', 1) -->a['a'] =1   
a.setdefault('a', 2) --> return 1  
   
b = [1,2,3,4,5]    
c = [x for x in b if x % 2 == 0] --> c = [2, 4]
