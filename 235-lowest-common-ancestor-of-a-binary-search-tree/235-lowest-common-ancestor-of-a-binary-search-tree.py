# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Runtime: O(logn or h), height of the tree
        Space: O(1)
        """
        if root is None:
            return None
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        elif root.val == p.val:
            return p
        elif root.val == q.val:
            return q