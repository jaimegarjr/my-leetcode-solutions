class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Runtime: O(n^2 + nlogn)
        # Space: O(n)
        nums.sort()
        triplets = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.findTriplets(i, i + 1, len(nums)-1, triplets, nums)
            
        return triplets
    
    
    def findTriplets(self, i, l, r, triplets, nums):
        while l < r:
            triplet = [nums[i], nums[l], nums[r]]
            curSum = nums[i] + nums[l] + nums[r]
            
            if curSum > 0:
                r -= 1
            elif curSum < 0:
                l += 1
            
            else:
                triplets.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            
        return