class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """
        Returns the city with the least amount of cities that are reachable with distance less than threshold
        Runtime: O(v*elogv), dijkstras for each node v, where dijkstras runtime is elogv
        Space: O(v+e)
        """
        graph = {i:[] for i in range(n)}
        
        for u, v, wt in edges:
            graph[u].append((v, wt))
            graph[v].append((u, wt))
            
        def dijkstras(city):
            dist = [float('inf')] * n
            dist[city] = 0
            heap = []
            heapq.heappush(heap, (0, city))
            
            while heap:
                dis, node = heapq.heappop(heap)
                
                for adj in graph[node]:
                    adj_c, adj_d = adj
                    if adj_d + dis < dist[adj_c]:
                        dist[adj_c] = adj_d + dis
                        heapq.heappush(heap, (dist[adj_c], adj_c))
            
            return dist
        
        count = [0] * n
        res = 0
        for city in range(n):
            distance = dijkstras(city)
            for dis in distance:
                if dis <= distanceThreshold:
                    count[city] += 1
            if count[city] <= count[res]:
                res = city
        
        return res