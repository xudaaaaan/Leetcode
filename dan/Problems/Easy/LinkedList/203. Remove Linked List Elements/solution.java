/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if(head == null)
            return head;
            
        ListNode cur = head;
        while(cur != null && cur.next != null){
            while(cur.next != null && cur.next.val == val)
                cur.next = cur.next.next;
            cur = cur.next;  
        }
        return head.val == val? head.next : head;
    }
}
