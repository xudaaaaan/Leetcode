# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #fast is the last of the first list
        cur, pre = slow.next, None
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next, pre, cur = pre, cur, nxt
        #Merge two linkedlist
        node1, node2 = head, pre
        
        while node1 and node2:
            nxt = node1.next
            node1.next = node2
            node1, node2 = node2, nxt
       
