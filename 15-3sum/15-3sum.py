class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Runtime: O(n^2 + nlogn)
        # Space: O(n)
        nums.sort()
        triplets = []
        
        for i in range(len(nums)-2):
            self.findTriplets(i, i + 1, len(nums)-1, triplets, nums)
            
        return triplets
    
    
    def findTriplets(self, i, l, r, triplets, nums):
        while l < r:
            triplet = [nums[i], nums[l], nums[r]]
            curSum = sum(triplet)
            
            if curSum == 0 and triplet not in triplets:
                triplets.append(triplet)
                l += 1
            elif curSum < 0:
                l += 1
            else:
                r -= 1
        return