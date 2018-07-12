# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
        current, previous = slow.next, slow
        while current:
            nextNode = current.next
            current.next, previous, current = previous, current, nextNode
        tail = previous
        while head != tail:
            if head.val != tail.val:
                return False
            elif head.next == tail:
                break
            else:
                head, tail = head.next, tail.next
        return True
        
        
