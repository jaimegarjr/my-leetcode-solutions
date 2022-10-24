class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Runtime: O(n)
        Space: O(1)
        """
        coins = n
        for i in range(1, n+1):
            coins -= i
            if coins == 0:
                return i
            elif coins < 0:
                return i -1