# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cur, a, i = head, ListNode(0), 1
        a.next = cur
        while i < m:
            a, cur = cur, cur.next
            i += 1
        pre = None
        while cur or i > n:
            if i > n:
                tail = a.next
                a.next = pre
                tail.next = cur
                break
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
            i += 1
        return head if m > 1 else a.next
    
        
