class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Recursive + Memoization Soln.
        Runtime: O(n), n recursive calls
        Space: O(n), cache and recursion stack
        
        
        memo = [0] * len(nums)
        
        def robFrom(i, nums):
            if i >= len(nums):
                return 0
            if memo[i]:
                return memo[i]
            
            memo[i] = max(robFrom(i + 2, nums) + nums[i], robFrom(i + 1, nums))
            return memo[i]
                
        return robFrom(0, nums)
        """
        
        """
        DP Bottom Up
        Runtime: O(n)
        Space: O(n)
        
        if not nums:
            return 0
        
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        
        for i in range(N - 2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
        
        return maxRobbedAmount[0]
        """
        
        """
        DP Optimized
        Runtime: O(n)
        Space: O(1)
        """
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n + 1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
        
        