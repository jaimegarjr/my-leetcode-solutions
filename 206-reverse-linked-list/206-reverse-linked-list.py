# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Runtime: O(n)
        # Space: O(1)
        cur, prev = head, None
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = prev
            prev = tmp

        return prev