# Problem 206
[Link](https://leetcode.com/problems/reverse-linked-list/description/)

# Trick
As in a linked list, a node can only point to its next node. So in order to change its pointer to its previous node, we should use a value to store its previous value while traversing the list;  
Also, after changing a node's next pointer, its original next node will be lost. So we also should keep track of its next node, and store it in a variable before changing the direction of its next pointer.  

Two ways: iterative and recursive.
