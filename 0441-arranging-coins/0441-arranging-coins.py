class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Exhaustive iterative soln
        Runtime: O(n)
        Space: O(1)
        
        Binary Search soln
        Runtime: O(logn)
        Space: O(1)
        """
        left, right = 1, n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            coins = (mid * (mid + 1)) // 2
            
            if coins > n:
                right = mid - 1
            else:
                res = max(mid, res)
                left = mid + 1
        
        return res