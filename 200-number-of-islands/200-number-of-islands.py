class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Runtime: O(n)
        # Space: O(n)
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r,c):
            if (r >= ROWS or c >= COLS or
               r < 0 or c < 0 or
               (r, c) in visited or grid[r][c] == "0"):
                return
            
            visited.add((r,c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands