class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Runtime: O(n)
        Space: O(1)
        """
        total = 0
        maxSum = nums[0]
        
        for n in range(len(nums)):
            if total < 0:
                total = 0
            total += nums[n]
            maxSum = max(maxSum, total)
            
            
        return maxSum
            