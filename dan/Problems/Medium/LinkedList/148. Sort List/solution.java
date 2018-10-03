/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    //Quicksort
    public ListNode sortList1(ListNode head) {
        return quickSort(head, null);
    }
    
    public ListNode quickSort(ListNode head, ListNode tail){
        if(head == tail || head.next == null)
            return head;
        ListNode i = head;
        ListNode j = head.next;
        int x = i.val;
        while(j != null){
            while(j != null && j.val >= x){
                j = j.next;
            }
            if(j != null){
                i = i.next;
                int t = i.val; i.val = j.val; j.val = t;
                j = j.next;
            }
        }
        int m = i.val; i.val = head.val; head.val = m;
        quickSort(head, i);
        quickSort(i.next, tail);
        return head;
    }
    
    //Merge sort
    public ListNode sortList(ListNode head){
        if(head == null || head.next == null)
            return head;
        //Find the middle node
        ListNode fast = head;
        ListNode slow = head;
        ListNode pre = null;
        while(fast != null && fast.next != null){
            pre = slow;
            fast = fast.next.next;
            slow = slow.next;
        }
        pre.next = null;
        return merge(sortList(head), sortList(slow));
    }
    
    public ListNode merge(ListNode h1, ListNode h2){
        if(h1 == null || h2 == null)
            return h1 == null? h2:h1;

        if(h1.val <= h2.val){
            h1.next = merge(h1.next, h2);
            return h1;
        }else{
            h2.next = merge(h1, h2.next);
            return h2;
        }
        
    }
}
