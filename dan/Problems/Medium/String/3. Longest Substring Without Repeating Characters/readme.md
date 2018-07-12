# Problem 3
[Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

# Trick
Difficult for me. :(  
Use a dictionary as "slide window" which contains used chars, and will be updated when a new char is checked.  
if the char exists in the dic, than revise the "start" pointer;  
else, update l
