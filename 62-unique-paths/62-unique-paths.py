class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Recursive Soln
        if (m == 1 or n == 1):
            return 1
        
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        
        DP Soln
        Runtime: O(n * m)
        Space: O(n * m)
        
        dp = [[0] * n for _ in range(m)]
        
        for i in range(n):
            dp[m-1][i] = 1
        for i in range(m):
            dp[i][n-1] = 1
        
        for x in range(m - 2, -1, -1):
            for y in range(n - 2, -1, -1):
                dp[x][y] = dp[x + 1][y] + dp[x][y + 1]
        
        return dp[0][0]

        DP Soln (NeetCode)
        Runtime: O(n * m)
        Space: O(n)
        """
        row = [1] * n
        
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        
        return row[0]