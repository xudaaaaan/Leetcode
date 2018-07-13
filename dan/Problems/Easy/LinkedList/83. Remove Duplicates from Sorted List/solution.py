# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        while cur:
            tag = cur
            cur = cur.next
            while cur and cur.val == tag.val:
                tag.next, cur = cur.next, cur.next
        
        return head
