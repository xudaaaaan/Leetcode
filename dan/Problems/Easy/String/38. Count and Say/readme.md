# Problem 38
[Problem link](https://leetcode.com/problems/count-and-say/description/)
# Trick
No need to create an array to store the results of n lines, just use iteration and update the result for n times;
Keep track of the letter you can comparing to now, and only when the comparison result is False can you update the result variation and begin a new comparison(update "let" and "temp").
