# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        fast, slow, pre, nxt = head, head, None, head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            pre = slow
            slow = nxt
            nxt = slow.next
            slow.next = pre
        if fast.next:
            node1, node2 = slow, nxt
        else:
            node1, node2 = slow.next, nxt
        
        while node1 and node2:
            if not node1.val == node2.val:
                return False
            node1, node2 = node1.next, node2.next
        return True
            
            
            

        
        
