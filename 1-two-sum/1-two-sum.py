class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        X + Y = target
        Y = target - X
        1. iterate through nums
        2a. check if num in hash map, if so return indices
        2. store into hash map the above equation if not
        """
        
        pairs = {}
        
        for i in range(len(nums)):
            if nums[i] not in pairs:
                pairs[target - nums[i]] = i
            else:
                return [pairs[nums[i]], i]
        