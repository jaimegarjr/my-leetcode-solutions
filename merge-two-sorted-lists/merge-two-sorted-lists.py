# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(next=list1)
        trav = head
        l1, l2 = list1, list2
        
        while l1 and l2:
            if l1.val < l2.val:
                trav.next = l1
                l1 = l1.next
            
            else:
                trav.next = l2
                l2 = l2.next
            
            trav = trav.next
                
        
        if not l2:
            trav.next = l1
        else:
            trav.next = l2
        
        return head.next