class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Runtime: O(n * m)
        Space: O(n + m)
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [0] * ROWS, [0] * COLS
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = 1
                    cols[c] = 1
        
        for r in range(len(rows)):
            if rows[r] == 1:
                for i in range(COLS):
                    matrix[r][i] = 0
                    
        for c in range(len(cols)):
            if cols[c] == 1:
                for i in range(ROWS):
                    matrix[i][c] = 0