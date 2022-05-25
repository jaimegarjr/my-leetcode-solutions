class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Runtime: O(n*m)
        Space: O(n*m)
        """
        ROWS, COLS = len(image), len(image[0])
        oldColor = image[sr][sc]
        
        def dfs(sr, sc):
            if (sr < 0 
                or sc < 0 
                or sr >= ROWS 
                or sc >= COLS 
                or image[sr][sc] != oldColor 
                or image[sr][sc] == newColor):
                return image # if out of bounds, not equal to color, or already is the color
            else:
                image[sr][sc] = newColor # reassign
                dfs(sr-1, sc) # top
                dfs(sr+1, sc) # bottom
                dfs(sr, sc-1) # left
                dfs(sr, sc+1) # right
        
        dfs(sr, sc)
        return image