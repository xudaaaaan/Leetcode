[Problem 130](https://leetcode.com/problems/surrounded-regions/description/)
#Trick
First traverse the borders of the grid, dfs each "O" on the border and the "O"s next to them, and mark them as "visited";
Then traverse the whole grid and change the unvisited "O"s to "X".  

The initialization of a 2D list:  
a = [[0] * 3] * 4  
Then each line in a will be the same!! Even if you change only a[2][1] to 1, the list will become: [[0,1,0,0],[0,1,0,0],[0,1,0,0]].  
To avoid this, a = [[0 for _ in range(3)] for _ in range(4)]  
