# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        node = head
        while node:
            h = node
            cnt = 1
            while cnt < k and node:
                node = node.next
                cnt += 1
            if node:
                cnt = 1
                prev, cur = None, h
                while cnt <= k:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cnt += 1
                    cur = nxt
                node = cur
                p.next = prev
                p = h
            else:
                p.next = h
        return dummy.next
            
