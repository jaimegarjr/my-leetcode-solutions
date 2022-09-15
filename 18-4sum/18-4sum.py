class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds the sum of 4 nums that equals 0
        Runtime: O(n^3)
        Space: O(n), for sorting
        """
        res = []
        nums.sort()

        for i in range(len(nums)-3):  # O(n)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            otherSum = target - nums[i]
            triplets = self.threeSum(nums[i+1:], otherSum)  # O(n^2)
            for t in triplets:
                res.append([nums[i]] + t)

        return res


    def threeSum(self, nums, target):
        """
        Finds the sum of 3 nums that equals 0
        Runtime: O(n^2)
        """
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.findTriplets(res, nums, i, i + 1, len(nums)-1, target)

        return res


    def findTriplets(self, triplets, nums, i, l, r, target):
        while l < r:
            curSum = nums[i] + nums[l] + nums[r]
            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                triplets.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while r > l and nums[r] == nums[r+1]:
                    r -= 1