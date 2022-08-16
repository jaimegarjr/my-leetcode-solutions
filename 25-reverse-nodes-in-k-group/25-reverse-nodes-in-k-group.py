# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev, cur = dummy, head
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            prev = kth.next
            for i in range(k):
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next
    
    def getKth(self, node, k):
        tmp, i = node, 0
        
        while tmp and i < k:
            tmp = tmp.next
            i += 1
            
        return tmp