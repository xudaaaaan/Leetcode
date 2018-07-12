# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res, c = ListNode(0), 0
        head = res
        while l2 or l1:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            t = l1_val + l2_val + c
            c = 1 if t >= 10 else 0
            t = t if t < 10 else (t - 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res.next = ListNode(t)
            res = res.next
        if c == 1:
            res.next = ListNode(c)
        return head.next
