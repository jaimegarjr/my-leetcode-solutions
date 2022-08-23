class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Runtime: O(n)
        # Space: O(1)
        maxWater = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            length = min(height[l], height[r])
            width = r - l
            area = length * width
            maxWater = max(maxWater, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater