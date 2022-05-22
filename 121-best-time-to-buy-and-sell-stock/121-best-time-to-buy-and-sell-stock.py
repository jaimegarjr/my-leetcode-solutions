class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Runtime: O(n)
        Space: O(1)
        """
        maxProfit = 0
        l, r = 0, 1
        
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
                
            r = r + 1

        return maxProfit