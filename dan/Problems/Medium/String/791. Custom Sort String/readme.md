# Problem 791
[Link](https://leetcode.com/problems/custom-sort-string/description/)

# Trick
1 Use sorted(ls, key)   
2 Use Counter()   
import collections   
C = collections.Counter("aabvdvd")    
C['a'] -->> 2    
C.update("abc")   
C['a']  -->>3
C.subtract("aaa")    
C['a'] -->> 0   
del C["a"]    
C -->> Counter({'b':1, 'v':2, 'd':1})   
list(C.elements()) -->> {b,v,v,d,d}    
c.items() -->> [('b', 1), ('v', 2), ('d', 1)]  convert to 2-d list  



