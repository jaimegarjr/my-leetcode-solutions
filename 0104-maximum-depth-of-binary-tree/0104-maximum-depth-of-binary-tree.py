# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Computes max depth of a BST given as root
        Runtime: O(n)
        Space: O(n)
        """
        if not root:
            return 0
        maxDepth = 0
        q = collections.deque([root])

        while q:
            level = len(q)
            for _ in range(level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            maxDepth += 1

        return maxDepth