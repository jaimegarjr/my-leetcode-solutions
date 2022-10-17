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
        left, right = 0, n
        
        while left <= right:
            k = (left + right) // 2
            cur = (k * (k + 1)) // 2
            
            if cur == n:
                return k
            if cur < n:
                left = k + 1
            else:
                right = k - 1
        
        return right