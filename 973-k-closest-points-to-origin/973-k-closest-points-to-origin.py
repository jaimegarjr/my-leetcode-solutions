class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for x, y in points:
            point = [(x ** 2) + (y ** 2), x, y]
            distances.append(point)
        
        heapq.heapify(distances)
        
        while k > 0:
            res.append(heapq.heappop(distances)[1:])
            k -= 1
        
        return res