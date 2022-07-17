class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Runtime: O(v + e)
        Space: O(v + e)
        """
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            
            neighs = adj[i]
            for neigh in neighs:
                if neigh == prev:
                    continue
                if not dfs(neigh, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n