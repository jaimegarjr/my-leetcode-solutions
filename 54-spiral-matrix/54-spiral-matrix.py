class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Runtime: O(n * m)
        # Space: O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        l, r, t, b = 0, COLS, 0, ROWS
        
        while l < r and t < b:
            # left to right
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            
            # top to bottom
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1
            
            if not (l < r and t < b):
                break
            
            # right to left
            for i in range(r-1, l-1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            
            # bottom to top
            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            
        return res
        