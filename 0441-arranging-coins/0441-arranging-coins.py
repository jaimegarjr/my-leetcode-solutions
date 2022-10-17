class Solution:
    def arrangeCoins(self, n: int) -> int:
        res, i = 0, 1
        while n > 0:
            n -= i
            i += 1
            res += 1
        
        if n < 0:
            res -= 1
        
        return res