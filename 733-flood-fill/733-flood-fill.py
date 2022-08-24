class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        if oldColor == color:
            return image
        
        def bfs(r, c):
            q = collections.deque([(r, c)])
            
            while q:
                row, col = q.popleft()
                image[row][col] = color
                
                directions = [
                    (-1, 0),
                    (0, 1),
                    (1, 0),
                    (0, -1)
                ]
                for x, y in directions:
                    dr = row + x
                    dc = col + y
                    if (dr in range(ROWS) and
                       dc in range(COLS) and
                       image[dr][dc] == oldColor):
                        q.append((dr, dc))
        
        bfs(sr, sc)
        return image