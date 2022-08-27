class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Runtime: O(klogn)
        # Space: O(n)
        distances = []
        res = []
        for x, y in points: # n
            point = [math.sqrt((x ** 2) + (y ** 2)), x, y]
            distances.append(point)
        
        heapq.heapify(distances) # n
        
        while k > 0: # klogn
            res.append(heapq.heappop(distances)[1:])
            k -= 1
        
        return res