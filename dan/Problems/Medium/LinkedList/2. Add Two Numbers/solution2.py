# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        c = 0
        while l1 or l2 or c:
            res.next = ListNode(0)
            res = res.next
            if l1 and l2:
                res.val = l1.val + l2.val + c
                l1, l2 = l1.next, l2.next
            elif l1:
                res.val = l1.val + c
                l1 = l1.next
            elif l2:
                res.val = l2.val + c
                l2 = l2.next
            else:
                res.val = c
            c = 0
            if res.val >= 10:
                res.val -= 10
                c = 1
        
        return head.next
        
