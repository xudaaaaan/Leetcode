# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node = head.next
        head.next = head.next.next
        node.next = head
        head = node
        node = node.next
        while node.next and node.next.next:
            t = node.next.next
            node.next.next = t.next
            t.next = node.next
            node.next = t
            node = node.next.next
        return head
        
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next            
