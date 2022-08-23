# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Runtime: O(v+e)
        # Space: O(v+e)
        if not root:
            return root
        
        res = []
        q = collections.deque()
        q.append(root)
        zigZag = True
        
        while q:
            levelSize = len(q)
            level = collections.deque()
            
            for _ in range(levelSize):
                node = q.popleft()
                if zigZag:                    
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            zigZag = not zigZag
            res.append(level)
            
        return res