class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Runtime: O(v + e), DFS / adjacency list soln
        Space: O(v + e)
        
        count = 0
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node):
            for e in graph[node]:
                if not visited[e]:
                    visited[e] = True
                    dfs(e)
        
        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)
        
        return count
        """
        
        """
        Union Find soln
        """
        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            res = n1
            
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res