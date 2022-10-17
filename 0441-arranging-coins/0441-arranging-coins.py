class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Runtime: O(n)
        Space: O(1)
        res, i = 0, 1
        while n > 0:
            n -= i
            i += 1
            res += 1
        
        if n < 0:
            res -= 1
        
        return res
        """
        left, right = 1, n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            coins = (mid * (mid + 1)) // 2
            
            if coins == n:
                return mid
            if coins < n:
                left = mid + 1
            else:
                right = mid - 1
        
        return right