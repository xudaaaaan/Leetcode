#[96. Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/description/)
##Trick
Deduce a formula:  
Let G(n) represents the number of BST that stores 1... to n;  
Let F(i, n) (1 <= i <= n) represents the number of BST that stores 1 to n which has node i as its root; That means the left subtree of it consists of 1 ~ (i-1), and the right subtree of it consists of (i+1) ~ n.   
G(n) = F(1, n) + F(2, n) + ... + F(n, n)   
F(i, n) = G(i - 1) * G(n - i) (i > 1)   
G(0) = 1, G(1) = 1  
G(n) = G(0) * G(n - 1) + G(1) * G(n - 2) + G(2) * G(n - 3) + ... + G(n - 1) * G(0)   
So, G(n) depends on the values of G(1)... G(n - 1). Use dynammic programming to solve the problem is very natural.
