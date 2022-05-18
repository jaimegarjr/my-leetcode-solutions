class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Runtime: O(n)
        # Space: O(n)
        sum_map = {}
        
        for i in range(len(nums)):
            if nums[i] in sum_map:
                return [i, sum_map[nums[i]]]
            else:
                sum_map[target - nums[i]] = i
        