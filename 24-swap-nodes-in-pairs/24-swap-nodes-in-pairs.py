# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses adjacent nodes in a list
        head: Node
        rtype: Node
        """
        dummy = ListNode(0, next=head)
        d = dummy

        while d and d.next:
            k = getKth(d.next, 2)
            p = reverseList(d.next, k)
            newD = d.next
            newD.next = k
            d.next = p
            d = newD

        return dummy.next


def getKth(node, k):
    if not node:
        return None
    tmp = node
    for _ in range(k):
        if not tmp: break
        tmp = tmp.next
    return tmp


def reverseList(node, k):
    if not node:
        return None
    cur, prev = node, None

    while cur != k:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev