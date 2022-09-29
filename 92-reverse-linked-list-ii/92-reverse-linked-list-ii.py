# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverses adjacent nodes in a list
        head: Node
        rtype: Node
        """
        dummy = ListNode(0, next=head)
        d = dummy

        for _ in range(left - 1):
            d = d.next

        k = getKth(d.next, right - left + 1)
        p = reverseList(d.next, k)
        newD = d.next
        newD.next = k
        d.next = p

        return dummy.next


def getKth(node, k):
    tmp = node

    for _ in range(k):
        if not tmp:
            break
        tmp = tmp.next

    return tmp


def reverseList(node, k):
    cur, prev = node, None

    while cur != k:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev