# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        results = []
        def dfs(node, level):
            if level == len(results):
                results.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    results[level].append(node.val)
                else:
                    results[level].appendleft(node.val)
            
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        # normal level order traversal with DFS
        dfs(root, 0)

        return results