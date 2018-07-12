# Problem 264
[Link](https://leetcode.com/problems/ugly-number-ii/description/)

# Trick
ugly numbers can be classified as three class:   
1. 2*1, 2*2, 2*3, 2*4, 2*5 ...   
2. 3*1, 3*2, 3*3, 3*4, 3*5, ...    
3. 5*1, 5*2, 5*3, 5*4, 5*5, ...   
    So we can use the first element 1, get the next one: min(2, 3, 5), the minimum element of corresponding element at each collumn;    
    Then update the element at the column we just take the element, and begin the next comparison.
