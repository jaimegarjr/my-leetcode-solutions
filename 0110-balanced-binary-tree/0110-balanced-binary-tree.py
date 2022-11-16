# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a tree given as root is a height-balanced tree
        Runtime: O(v + e), or n nodes
        Space: O(h or n), where h is height 
        """

        def dfs(node):
            if not node:
                return (True, 0)

            leftStatus, leftHeight = dfs(node.left)
            rightStatus, rightHeight = dfs(node.right)

            if (leftStatus and rightStatus) and (abs(leftHeight - rightHeight) <= 1):
                return (True, max(leftHeight, rightHeight) + 1)

            return (False, -1)

        balanced, _ = dfs(root)
        return balanced