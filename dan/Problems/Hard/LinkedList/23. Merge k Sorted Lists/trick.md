#[Problem 23](https://leetcode.com/problems/merge-k-sorted-lists/description/)
#Trick
1.Find the largest one of the first nodes in each linkedlist. -> TLE   
2.Use PriorityQueue. Keep the first nodes of each linkedlist and return the larget one, which should have top priority, so this one process can cost O(log k) tiem. k is the number of linkedlist.  
3.Divide and conquer.Partition the lists into two equal part and find the sorted list of them respectively, and sort the two list finally.Use recursion. O(Nlogk) of time and O(1) of space.
