# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def dfs(root):
            if not root: return -1
            
            leftH = dfs(root.left) 
            rightH = dfs(root.right) 
            
            diameter[0] = max(diameter[0], leftH + rightH + 2)
            
            return max(leftH, rightH) + 1
    
        dfs(root)
        return diameter[0]