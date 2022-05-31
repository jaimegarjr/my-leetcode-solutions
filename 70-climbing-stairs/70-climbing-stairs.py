class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        
        def dfs(count):
            if count == n:
                return 1
            if count > n:
                return 0
            if memo[count] > 0:
                return memo[count]
            
            memo[count] = dfs(count + 1) + dfs(count + 2)
            return memo[count]
            
        return dfs(0)