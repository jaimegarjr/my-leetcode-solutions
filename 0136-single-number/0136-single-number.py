class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Runtime: O(n)
        Space: O(1)
        """
        n = nums[0]
        for num in nums[1:]:
            n ^= num
        
        return n