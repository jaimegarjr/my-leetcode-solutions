class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Runtime: O(n*m)
        Space: O(n*m)
        """
        ROWS, COLS = len(image), len(image[0])
        
        def dfs(image, sr, sc, curColor, newColor):
            if sr < 0 or sc < 0 or sr >= ROWS or sc >= COLS or image[sr][sc] != curColor:
                return image
            elif image[sr][sc] == newColor:
                return image
            else:
                oldColor = image[sr][sc]
                image[sr][sc] = newColor
                dfs(image, sr-1, sc, oldColor, newColor)
                dfs(image, sr+1, sc, oldColor, newColor)
                dfs(image, sr, sc-1, oldColor, newColor)
                dfs(image, sr, sc+1, oldColor, newColor)
        
        dfs(image, sr, sc, image[sr][sc], newColor)
        
        return image