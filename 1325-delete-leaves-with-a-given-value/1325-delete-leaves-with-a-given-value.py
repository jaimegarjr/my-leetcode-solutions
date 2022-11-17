# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Returns root without leaves = target
        Runtime: O(v + e), or n nodes
        Space: O(h), h = log(n), n nodes
        """

        def dfs(node):
            if not node:
                return None

            if not node.left and not node.right and node.val == target:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if not node.left and not node.right and node.val == target:
                return None

            return node

        return dfs(root)