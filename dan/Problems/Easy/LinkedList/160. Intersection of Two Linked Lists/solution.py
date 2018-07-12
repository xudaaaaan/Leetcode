# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        dic = {}
        while a:
            dic[a] = 1
            a = a.next
        while b:
            if b in dic:
                return b
            else:
                b = b.next
        return None
    
    def getIntersectionNode(self, headA, headB):
        a, b, flag = headA, headB, 2
        while a and b and flag:
            if a == b:
                return a
            if not a.next:
                a = headB
                flag -= 1
            else:
                a = a.next
            if not b.next:
                b = headA
            else:
                b = b.next
            
        return None
