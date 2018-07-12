# Problem 120
[Link](https://leetcode.com/problems/triangle/description/)

# Trick
Use dp:  
1 From bottom to top: m[i][j] = Triangle[i][j] + min(m[i+1][j], m[i+1][j+1])   
2 From up to bottom:    
m[i][j] = m[i - 1][j] + T[i][j], if j == 0   
m[i][j] = m[i - 1][j - 1] + T[i][j], if j == len(T[i]) - 1   
m[i][j] = min(m[i - 1][j - 1], m[i - 1][j]) + T[i][j],  other situations
