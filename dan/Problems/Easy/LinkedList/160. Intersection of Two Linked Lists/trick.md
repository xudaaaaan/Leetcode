#[160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1)
##Trick
1.Hashtable  
Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: if bi appears in the hash set, then bi is the intersection node.   
2.Two pointers   
Maintain two pointers pA and pB, initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B; similarly when pB reaches the end of a list, redirect it the head of A.
If at any point pA meets pB, then pA/pB is the intersection node.
