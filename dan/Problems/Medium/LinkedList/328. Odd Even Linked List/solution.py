# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd, even, even_start = head, head.next, head.next
        is_odd = True
        cur = head.next.next
        while cur:
            if is_odd:
                odd.next, odd = cur, cur
            else:
                even.next, even = cur, cur
            cur = cur.next
            is_odd = (not is_odd)
        even.next = None
        odd.next = even_start
        return head 
    
