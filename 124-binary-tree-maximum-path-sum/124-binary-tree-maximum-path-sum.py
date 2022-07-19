# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: O(n)
        Space: O(n)
        """
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)
            
            # if split
            split = root.val + leftMax + rightMax
            res[0] = max(res[0], split)
            
            # if not split
            noSplit = max(leftMax, rightMax)
            
            return root.val + noSplit
            
        dfs(root)
        return res[0]