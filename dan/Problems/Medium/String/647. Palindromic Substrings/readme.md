# Problem 647
[Link](https://leetcode.com/problems/palindromic-substrings/description/)

# Trick
1 Brute Solution: enumerate all substrings of the string, and judge if it is a palindromic string. Time complexity:O(n^3)   
2 Enumerate the center of each string, check substrings of each center from short to long. Time complexity: O(n^2)   
3 [Manacher algorithm](https://blog.csdn.net/dyx404514/article/details/42061017)
Time complexity: O(n) 
