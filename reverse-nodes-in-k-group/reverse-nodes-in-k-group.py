# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        p = dummy
        
        while True:
            kth = self.findKth(p, k)
            if not kth: break
            
            nxt = kth.next
            cur = p.next
            prev = None
            
            i = 0
            while i < k:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
                i += 1
            
            end = p.next
            p.next.next = nxt
            p.next = kth
            p = end
        
        return dummy.next
    
    def findKth(self, node, k):
        while k != 0 and node:
            node = node.next
            k -= 1
        return node