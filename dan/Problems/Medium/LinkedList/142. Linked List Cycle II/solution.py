# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #Space complexity:o(n)
    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node, dic = head, {}
        while node:
            if node in dic:
                return node
            dic[node] = 1
            node = node.next
        return None
    
    #Method2: two pointers
    def detectCycle(self, head):
        if not head:
            return None
        fast, slow, flag = head, head, False
        while fast.next and fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break
        slow = head
        while flag:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next
        return None


