# Problem 257
[Link](https://leetcode.com/problems/binary-tree-paths/description/)
# Trick:
1 dfs + stack
2 bfs + queue
3 recursion

How to use queue in Python:
import collections
q = collections.deque()
q.append(3)
q.append(4)
q.append(5)
q.popleft() -> 3
q.popleft() -> 4
