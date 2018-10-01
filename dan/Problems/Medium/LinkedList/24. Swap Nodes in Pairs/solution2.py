# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        init = ListNode(0)
        init.next = head
        pre, n1 = init, head
        while n1:
            n2 = n1.next
            if not n2:
                break
            nxt = n2.next
            n1.next, pre.next, n2.next = nxt, n2, n1
            pre, n1 = n1, nxt
        return init.next
