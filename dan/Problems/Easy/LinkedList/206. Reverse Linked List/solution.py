class Solution:
    #iterative
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head
        while cur:
            nex = cur.next
            cur.next, cur, pre = pre, nex, cur
        return pre
            
            
        
    #recursive
    def reverseList(self, head):
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

        
