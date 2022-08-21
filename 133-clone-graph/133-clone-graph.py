"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Runtime: O(v+e)
        # Space: O(n)
        if not node:
            return node
        
        created = {node.val: Node(node.val, [])}
        q = collections.deque()
        q.append(node)
        
        while q:
            cur = q.popleft()
            curClone = created[cur.val]

            for nei in cur.neighbors:
                if nei.val not in created:
                    created[nei.val] = Node(nei.val, [])
                    q.append(nei)
                
                curClone.neighbors.append(created[nei.val])
        
        return created[node.val]
        
