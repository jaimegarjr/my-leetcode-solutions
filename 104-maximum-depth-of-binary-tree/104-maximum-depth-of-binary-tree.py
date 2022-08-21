# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Runtime: O(n) (v + e)
        # Space: O(n), size of queue
        depth = 0
        if not root:
            return depth
        
        q = collections.deque()
        q.append(root)
        
        while q:
            levels = len(q)
            for _ in range(levels):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            depth += 1
        
        return depth