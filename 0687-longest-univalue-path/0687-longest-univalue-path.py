# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        Computes the longest path with equal nodes of a BST given as root
        Runtime: O(n), v + e
        Space: O(h), height of tree 
        """
        res = [0]

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)  # compute longest path on left
            right = dfs(root.right)  # compute longest path on right

            # include root in path if equal
            if root.left and root.left.val == root.val:
                left += 1
            else:
                left = 0
            if root.right and root.right.val == root.val:
                right += 1
            else:
                right = 0

            res[0] = max(res[0], left + right)

            return max(left, right)

        dfs(root)
        return res[0]