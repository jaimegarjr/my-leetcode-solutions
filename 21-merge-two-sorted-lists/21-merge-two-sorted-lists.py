# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: O(n)
        Space: O(n)
        """
        dummy = ListNode()
        t1, t2 = list1, list2
        trav = dummy
        
        while t1 and t2:
            if t2.val < t1.val:
                trav.next = t2
                t2 = t2.next
            else:
                trav.next = t1
                t1 = t1.next
                
            trav = trav.next
        
        if t1:
            trav.next = t1
        else:
            trav.next = t2
        
        return dummy.next