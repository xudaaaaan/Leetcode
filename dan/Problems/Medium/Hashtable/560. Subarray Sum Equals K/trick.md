#[Problem 560](https://leetcode.com/problems/subarray-sum-equals-k/description/)
##Trick
Use a dict to store the sum up to the ith element.  
As the sum between a[i] and a[j] can be computed by sum[j] - sum[i], if a[i:j] is correct, then k should be equal to sum[j] - sum[i].So every time we compute sum[j], check if (sum[j] - k) exists in the dic. IF so, add dict[sum[j] - k] to result. 
