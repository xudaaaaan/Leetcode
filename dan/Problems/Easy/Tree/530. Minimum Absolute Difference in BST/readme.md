# Problem 530
[Link](https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/)

# Trick
1 dfs/bfs + compare every two numbers
use zip() in python: zip(a, a[1:])
2 divide and conquer:
find the MAD of left child and right child, compare them with two other possibles: 1) min difference between root and left child 2)min difference between root and right child
