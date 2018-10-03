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
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        c = 0
        res = None
        while stack1 or stack2:
            node1, node2 = 0, 0
            if stack1:
                node1 = stack1.pop()
            if stack2:
                node2 = stack2.pop()
         
            tmp = node1 + node2 + c
            c = 0
            if tmp >= 10:
                tmp -= 10
                c = 1
            newNode = ListNode(tmp)
            newNode.next = res
            res = newNode
        if c:
            newNode = ListNode(c)
            newNode.next = res
            res = newNode
        return res
            
                
