/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    //my solution
    public ListNode getIntersectionNode1(ListNode headA, ListNode headB) {
        if(headA == null || headB == null)
            return null;
            
        ListNode cur1 = headA;
        ListNode cur2 = headB;
        int sup = 0;
        while(sup < 3){
            if(cur1 == cur2)
                return cur1;
            
            if(cur1.next == null){
                cur1 = headB;
                sup++;
            }else
                cur1 = cur1.next;
                
            if(cur2.next == null){
                cur2 = headA;
                sup++;
            }else
                cur2 = cur2.next;
                    
        }
        return null;
    }
    
    //smarter solution: if no intersection, cur1 and cur2 will meet with both the values are null.
    public ListNode getIntersectionNode(ListNode headA, ListNode headB){
        ListNode curA = headA;
        ListNode curB = headB;
        while(curA != curB){
            curA = curA==null?headB:curA.next;
            curB = curB==null?headA:curB.next;
        }
        return curA;
    }
}
