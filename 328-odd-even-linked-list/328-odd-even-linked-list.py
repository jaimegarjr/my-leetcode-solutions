# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Groups a linked list into even and odd groups
        head: Node
        rtype: Node
        """
        if not head or not head.next:
            return head
        o, e = head, head.next
        se = e
        t = e.next
        oddOrEven = True

        while t:
            if not oddOrEven:
                e.next = t
                e = t
            else:
                o.next = t
                o = t
            oddOrEven = not oddOrEven
            t = t.next

        e.next = None
        o.next = se

        return head