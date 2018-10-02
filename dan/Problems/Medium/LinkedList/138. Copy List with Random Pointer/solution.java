/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    //Use dictionary
    public RandomListNode copyRandomList1(RandomListNode head) {
        if(head == null)
            return null;
        HashMap<RandomListNode, RandomListNode> copy = new HashMap<RandomListNode, RandomListNode>();
        RandomListNode cur = head;
        RandomListNode head2 = new RandomListNode(head.label);
        RandomListNode cur2 = head2;
        while(cur != null){
            copy.put(cur, cur2);
            if (cur.next != null){
                cur2.next = new RandomListNode(cur.next.label);
                cur2 = cur2.next;
            }
            cur = cur.next; 
        }
        cur = head;
        while(cur != null){
            if(cur.random != null)
                copy.get(cur).random = copy.get(cur.random);
            cur = cur.next;
        }
        return head2;
    }
    
    //Add a node after each node
    public RandomListNode copyRandomList(RandomListNode head){
        if(head == null){
            return head;
        }
        RandomListNode cur = head;
        while(cur != null){
            RandomListNode nxt = cur.next;
            cur.next = new RandomListNode(cur.label);
            cur.next.next = nxt;
            cur = nxt;
        }
        cur = head;
        while(cur != null){
            if(cur.random != null)
                cur.next.random = cur.random.next;
            cur = cur.next.next;
        }
        cur = head;
        RandomListNode head2 = head.next;
        RandomListNode cur2 = head2;
        while(cur != null){
            cur.next = cur.next.next;
            cur = cur.next;
            if(cur != null){
                cur2.next = cur2.next.next;
                cur2 = cur2.next;
            }

        }
        return head2;
    }
}
