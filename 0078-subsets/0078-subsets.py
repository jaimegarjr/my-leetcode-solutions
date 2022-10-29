class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, comb):
            
            res.append(comb[:])
            for i in range(len(nums)):
                comb.append(nums[i])
                backtrack(nums[i+1:], comb)
                comb.pop()

        backtrack(nums, [])
        return res