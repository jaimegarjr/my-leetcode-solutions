class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Recursion w/ Memoization
        Runtime: O(n)
        Space: O(n)
        
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
        """
        
        """
        DP - Bottom Up
        Runtime: O(n)
        Space: O(1)
        """
        one, two = 1, 1
        
        for i in range(n - 1, 0, -1):
            tmp = one + two
            two = one
            one = tmp
            
        return one