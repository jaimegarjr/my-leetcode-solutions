# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        # DFS
        # Runtime: O(n)
        # Space: O(h or n)
        
        def isSameTree(p, q):
            if not p and not q: return True
            if (not p and q) or (not q and p) or (p.val != q.val): return False

            return isSameTree(p.right, q.left) and isSameTree(p.left, q.right)
        
        return isSameTree(root.left, root.right)
        """
        # BFS
        # Runtime: O(n)
        # Space: O(n)
        q = collections.deque([root.left, root.right])
        
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            
            if not t1 and not t2: continue
            if not t1 or not t2 or t1.val != t2.val: return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        
        return True
        
        