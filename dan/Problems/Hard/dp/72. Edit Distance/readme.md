#[Problem 72](https://leetcode.com/problems/edit-distance/submissions/1)
##Trick
Initiate an array dp[i][j] to store the number of steps needed to convert word1[0:i - 1] to word2[0:j - 1].  
dp[0][j] = j;  
dp[i][0] = i;  
dp[i][j]? Depends on if word1[i - 1] == word2[j - 1].  
if word1[i - 1] == word2[j - 1] : dp[i][j] = dp[i - 1][j - 1];   
else, we have three choices: replace, insert, and delete.  
Replace:replace word1[i - 1] with word2[j - 1]. dp[i][j] = dp[i - 1][j - 1] + 1;   
Insert: Insert word2[j - 1] to the end of word1[0:i - 1]. dp[i][j] = dp[i][j - 1] + 1;   
Delete: Delete word1[i - 1] so that word1[0:i - 2] == word2[0:j - 1]. dp[i][j] = dp[i - 1][j] + 1.   
Finally, dp[i][j] = min(insert, replace, delete).  
Return dp[len(word1)][len(word2)] at last.
