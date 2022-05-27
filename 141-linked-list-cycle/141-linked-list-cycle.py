# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Runtime: O(n)
        Space: O(1)
        """
        
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow.next and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            
            if not fast:
                break
        
        return False