# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        d, carry = res, 0
        t1, t2 = l1, l2

        while t1 and t2:
            addition = t1.val + t2.val + carry
            if addition >= 10:
                carry = 1
                d.next = ListNode(addition % 10)
            else:
                carry = 0
                d.next = ListNode(addition)
            t1, t2, d = t1.next, t2.next, d.next

        trav = t2 if not t1 else t1

        while trav:
            addition = carry + trav.val
            if addition >= 10:
                carry = 1
                d.next = ListNode(addition % 10)
            else:
                carry = 0
                d.next = ListNode(addition)
            trav, d = trav.next, d.next

        if carry == 1:
            d.next = ListNode(carry)

        return res.next