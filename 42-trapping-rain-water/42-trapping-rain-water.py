class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        leftMax, rightMax = 0, 0
        
        while l <= r:
            # update maxes
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            
            # determine if dip, update res if so
            if height[l] < leftMax:
                side = min(leftMax, rightMax)
                res += side - height[l]
            
            if l == r: break
            
            if height[r] < rightMax:
                side = min(leftMax, rightMax)
                res += side - height[r]
            
            # update pointers
            if leftMax < rightMax: 
                l += 1
            elif rightMax < leftMax: 
                r -= 1
            else: 
                l += 1
                r -= 1
        
        return res