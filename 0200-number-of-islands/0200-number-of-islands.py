class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Runtime: O(v + e)
        Space: O(n)
        """
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r >= rows or
                r < 0 or
                c >= cols or
                c < 0 or
                (r, c) in visited or
                    grid[r][c] == "0"):
                return

            visited.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands