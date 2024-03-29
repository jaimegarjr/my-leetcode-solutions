# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Runtime: O(n)
        Space: O(1)
        """
        dummy = ListNode(-1, next=head)
        
        trav = dummy
        while trav.next:
            if trav.next.val == val:
                trav.next = trav.next.next
            else:
                trav = trav.next
        
        return dummy.next