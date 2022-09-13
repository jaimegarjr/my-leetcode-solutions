class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s, e = 0, 1
        total = 0
        
        for _ in range(len(nums) // 2):
            total += min(nums[s], nums[e])
            s += 2
            e += 2
        return total