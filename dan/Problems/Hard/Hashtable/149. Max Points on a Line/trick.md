#[Problem 149](https://leetcode.com/problems/max-points-on-a-line/submissions/1)
##Trick
1 y = kx + b, using (k, b) to represent a line is not a good idea, because k can be infinete, and float number may cause some unexpected wrong.(automatically truncated when float numbers are very very large.)  
2 Fix one point, only store the k value of other pointsm with this fixd points. To store k as integers, we can use (y1 - y2, x1 - x2) tuple. And we have to compute the gcd of y1 - y2 and x1 - x2.   
3 gcd(y, x - y) contains more steps than gcd(y, x % y). So give the second way more priority.
