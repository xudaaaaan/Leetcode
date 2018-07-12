# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = ListNode(0)
        head = a
        while l1 and l2:
            if l1.val < l2.val:
                a.next = ListNode(l1.val)
                l1 = l1.next
            else:
                a.next = ListNode(l2.val)
                l2 = l2.next
            a = a.next
        if l1:
            a.next = l1
        else:
            a.next = l2
        return head.next
    
    #Recursive
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
            
                
            
            
            
            
            
          
