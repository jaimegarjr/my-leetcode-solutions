# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree given root
        Runtime: O(n), v + e
        Space: O(h), height of tree 
        """
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            root.left, root.right = root.right, root.left

        dfs(root)
        return root