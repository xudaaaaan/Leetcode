# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        node, cnt = head, 1
        while cnt < n:
            node = node.next
            cnt += 1
        if node.next:
            node = node.next
            npre_node = head
            while node.next:
                node = node.next
                npre_node = npre_node.next
            npre_node.next = npre_node.next.next
            return head
            
        else:
            return head.next
