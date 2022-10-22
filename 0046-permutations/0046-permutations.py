class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Gets all the permutations of a given nums
        Runtime: O(n!)
        Space: O(n!)
        """
        res = []

        def dfs(nums, perm):
            if not nums:
                res.append(perm[:])

            for i in range(len(nums)):
                newN = nums[0:i] + nums[i+1:]
                perm.append(nums[i])
                dfs(newN, perm)
                perm.pop()

        dfs(nums, [])
        return res