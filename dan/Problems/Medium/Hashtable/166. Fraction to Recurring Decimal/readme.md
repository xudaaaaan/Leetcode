[Problem 166](https://leetcode.com/problems/fraction-to-recurring-decimal/description/)

#Trick
divmod(a,b) =>> [a // b, a % b]   
Using while loop to find the repeated parts. Notice that only when the remainder is the same that the repeated part appears.
