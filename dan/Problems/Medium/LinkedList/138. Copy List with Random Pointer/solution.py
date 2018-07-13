# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    #O(n) space complexity
    def copyRandomList1(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = {}
        node = head
        while node:
            dic[node] = RandomListNode(node.label)
            node = node.next
        node = head
        while node:
            dic[node].next = dic.get(node.next)
            dic[node].random = dic.get(node.random)
            node = node.next
        return dic.get(head)  
    
    
    #O(1) space cmoplexity
    def copyRandomList(self, head):
        if not head:
            return None
        
        #insert a node after each node in the list
        cur = head
        while cur:
            nxt = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next, cur = nxt, nxt
        cur = head
        
        #Allocate random pointers
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        #Seperate two lists
        cur = second = head.next
        while cur and cur.next:
            head.next = cur.next
            cur.next = cur.next.next
            cur, head = cur.next, head.next
        head.next = None
            
        return second
