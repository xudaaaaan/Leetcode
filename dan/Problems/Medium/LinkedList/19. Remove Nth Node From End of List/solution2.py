# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #one-pass solution
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        fast, slow, pre = head, head, None
        for i in range(n - 1):
            fast = fast.next
        while fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next
        if pre:
            pre.next = pre.next.next
            return head
        else:
            return head.next
            
