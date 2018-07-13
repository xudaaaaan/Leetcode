# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #quick sort
    def sortList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.sort(head, None)
    
    def sort1(self, begin, end):
        if not begin or begin.next == end or begin == end:
            return begin
        i, j, x = begin, begin.next, begin.val
        while j is not end:
            while j is not end and j.val >= x:
                j = j.next
            if j is not end:
                i = i.next
                i.val, j.val = j.val, i.val
                j = j.next
        begin.val, i.val = i.val, begin.val
        self.sort(begin, i)
        self.sort(i.next, end)
        return begin
    #merge sort
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))


