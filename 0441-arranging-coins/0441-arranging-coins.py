class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Runtime: O(logn)
        Space: O(1)
        """
        l, r = 0, n
        res = 0
        
        while l <= r:
            m = (l + r) // 2
            coins = (m * (m+1)) // 2
            
            if coins <= n:
                res = max(m, res)
                l = m + 1
            else:
                r = m - 1
        
        return res