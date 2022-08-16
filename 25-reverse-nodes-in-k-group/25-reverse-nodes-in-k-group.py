# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        
        while self.getKth(leftPrev, k):
            prev = None

            for i in range(k):
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            
            leftPrev.next.next = cur
            tmp = leftPrev.next
            leftPrev.next = prev
            leftPrev = tmp
        
        return dummy.next
    
    def getKth(self, node, k):
        tmp, i = node, 0
        
        while tmp and i < k:
            tmp = tmp.next
            i += 1
            
        if tmp:
            return tmp
        else:
            return None