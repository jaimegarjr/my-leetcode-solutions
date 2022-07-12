class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Runtime: O(nm)
        Space: O(nm)
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        zeros = {}
    
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeros[(r,c)] = 0
        
        for z in zeros.keys():
            r, c = z[0], z[1]
            
            for i in range(COLS):
                matrix[r][i] = 0
                
            for i in range(ROWS):
                matrix[i][c] = 0