# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Runtime: O(n, or v+e)
        # Space: O(n)
        res = []
        
        if not root:
            return None
        
        q = collections.deque()
        q.append(root)
        
        while q:
            levels = len(q)
            level = []
            
            for _ in range(levels):
                node = q.popleft()
                if node:
                    level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level)
        
        return res