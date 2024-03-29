class Solution:
    def trap(self, height: List[int]) -> int:
        # Runtime: O(n)
        # Space: O(1)
        if not height: return 0
        res = 0
        l, r = 0, len(height)-1
        leftMax, rightMax = 0, 0
        
        while l < r:
            # determine if dip, update res if so
            if height[l] < leftMax:
                res += leftMax - height[l]
            
            if height[r] < rightMax:
                res += rightMax - height[r]
            
            # update maxes
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            
            # update pointers
            if leftMax <= rightMax: 
                l += 1
            else: 
                r -= 1
        
        return res