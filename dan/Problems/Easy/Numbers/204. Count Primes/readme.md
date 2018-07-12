[Problem 204](https://leetcode.com/problems/count-primes/description/)
#Trick
Initiate a list to record each integer's status(1 is prime and 0 is not prime).Then find each composite number and change their list values to 0. Finally, sum up the list.  
How to find each composite number? Using multiple relations. Avoid repeated calculations.
