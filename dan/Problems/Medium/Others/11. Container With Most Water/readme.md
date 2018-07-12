# Problem 11
[Link](https://leetcode.com/problems/container-with-most-water/description/)

# Trick
i = 0, j = n - 1, and area(i, j) means area between the ith and jth column.
if a[i] < a[j], then area(i, k) where i < k < j must be smaller than area[i, j], so move i to i + 1, j unchanged.
