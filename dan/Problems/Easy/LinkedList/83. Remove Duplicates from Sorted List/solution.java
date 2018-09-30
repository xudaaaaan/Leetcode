/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    //My solution
    public ListNode deleteDuplicates1(ListNode head) {
        ListNode cur = head;
        while(cur != null && cur.next != null){
            ListNode nxt = cur.next;
            while(cur.val == nxt.val){
                cur.next = nxt.next;
                nxt = cur.next;
                if(nxt == null){
                    break;
                }
            }
            cur = nxt;
        }
        return head;
    }
    //Nicer solution
    public ListNode deleteDuplicates(ListNode head){
        ListNode cur = head;
        while(cur != null){
            if(cur.next == null){
                break;
            }
            if(cur.next.val == cur.val){
                cur.next = cur.next.next; 
            }else{
                cur = cur.next;
            }
        }
        return head;
    }
    
}
