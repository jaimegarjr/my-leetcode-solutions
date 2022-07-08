# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        
        while fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is None:
                return slow
        
        return slow.next
        