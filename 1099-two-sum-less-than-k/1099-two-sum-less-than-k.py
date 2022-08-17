class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        underKMax = -1
        left, right = 0, len(nums)-1
        
        nums.sort()
        
        while left < right:
            curSum = nums[left] + nums[right]
            
            if curSum >= k:
                right -= 1
            else:
                underKMax = max(curSum, underKMax)
                left += 1
        
        print(nums)
        
        return underKMax