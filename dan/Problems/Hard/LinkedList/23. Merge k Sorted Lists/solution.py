# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    #Time complexity: O(kN) where k is #of linkedlist and N is #of node. 
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        sm = 0
        for i in range(1, len(lists)):
            if lists[i] and (not lists[sm] or lists[i].val < lists[sm].val) :
                sm = i
        if not lists[sm]:
            return None
        node = lists[sm]
        lists[sm] = lists[sm].next
        node.next = self.mergeKLists(lists)
        return node
    
    #Priority Queue. Time complexity: O()
    def mergeKLists(self, lists):
        head = ListNode(0)
        point = head
        pq = PriorityQueue()
        for node in lists:
            if node:
                pq.put((node.val, node))

        while not pq.empty():
            val, node = pq.get()
            head.next = node
            head = head.next
            if node.next:
                node = node.next
                pq.put((node.val, node))
        return point.next
            
        
        
        
