class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        if oldColor == color:
            return image
        
        def dfs(r, c):
            if (r >= ROWS or
                r < 0 or
                c < 0 or
                c >= COLS or
                image[r][c] != oldColor):
                return
            
            image[r][c] = color
            directions = [
                (-1, 0),
                (0, 1),
                (1, 0),
                (0, -1)
            ]
            for x, y in directions:
                dfs(r+x, c+y)
        
        dfs(sr, sc)
        return image