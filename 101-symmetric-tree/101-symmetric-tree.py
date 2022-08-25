# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Runtime: O(n)
        # Space: O(h or n)
        def isSameTree(p, q):
            if not p and not q: return True
            if (not p and q) or (not q and p) or (p.val != q.val): return False

            return isSameTree(p.right, q.left) and isSameTree(p.left, q.right)
        
        return isSameTree(root.left, root.right)
    
        