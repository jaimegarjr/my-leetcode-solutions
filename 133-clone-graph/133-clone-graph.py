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
        
        created = {node: Node(node.val, [])}
        q = collections.deque()
        q.append(node)
        
        while q:
            cur = q.popleft()
            curClone = created[cur]

            for nei in cur.neighbors:
                if nei not in created:
                    created[nei] = Node(nei.val, [])
                    q.append(nei)
                
                curClone.neighbors.append(created[nei])
        
        return created[node]
        
