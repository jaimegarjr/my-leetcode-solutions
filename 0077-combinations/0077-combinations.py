class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        res = []

        def backtrack(nums, comb):
            if len(comb) == k:
                res.append(comb[:])

            for i in range(len(nums)):
                newN = nums[i+1:]
                comb.append(nums[i])
                backtrack(newN, comb)
                comb.pop()

        backtrack(nums, [])
        return res