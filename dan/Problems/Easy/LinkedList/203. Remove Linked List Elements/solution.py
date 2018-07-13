# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        while head and head.val == val:
            head = head.next
        
        if head:
            pre, cur = head, head.next
            while cur:
                while cur and cur.val == val:
                    pre.next, cur = cur.next, cur.next
                if cur:
                    pre, cur = cur, cur.next
        return head
