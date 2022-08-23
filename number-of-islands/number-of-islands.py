class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Runtime: O(v+e)
        # Space: O(n)
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                (r, c) in visited or 
                grid[r][c] == "0"):
                return
            
            visited.add((r, c))            
            directions = [
                (-1, 0),
                (0, 1),
                (1, 0),
                (0, -1)
            ]
            for x, y in directions:
                dfs(r + x, c + y)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count