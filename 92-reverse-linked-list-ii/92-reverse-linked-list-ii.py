# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        
        # finding beg list
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        # reversal
        prev = None
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        
        # clean up
        leftPrev.next.next = cur
        leftPrev.next = prev
        
        return dummy.next
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur = head
        prev = None
        
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev