class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Runtime: O(e*v)
        Space: O(v+e)
        """

        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmpP = prices[:]

            for s, d, p in flights:  # src, dst, price
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpP[d]:
                    tmpP[d] = prices[s] + p

            prices = tmpP
        return prices[dst] if prices[dst] != float('inf') else -1