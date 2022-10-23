class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Gets all the permutations of a given nums
        Runtime: O(n!)
        Space: O(n!)
        """
        res = []

        def backtrack(nums, perm):
            if not nums:
                res.append(perm[:])

            for i in range(len(nums)):
                newN = nums[0:i] + nums[i+1:]
                perm.append(nums[i])
                backtrack(newN, perm)
                perm.pop()

        backtrack(nums, [])
        return res