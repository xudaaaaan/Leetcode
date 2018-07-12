#[Problem 746](https://leetcode.com/problems/min-cost-climbing-stairs/description/)

#Trick
dp[i]: Cost needed to get to the ith step.(!!cost[i] isn't included)  
dp[0], dp[1] = 0, 0  
dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])  
return dp[len(cost)]
