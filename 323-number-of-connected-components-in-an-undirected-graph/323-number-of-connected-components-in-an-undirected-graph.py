class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Runtime: O(v + e), DFS / adjacency list soln
        Space: O(v + e)
        """
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