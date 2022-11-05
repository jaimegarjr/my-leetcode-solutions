class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Returns the max time to send a signal to all nodes from node k
        Runtime: O(v+e)
        Space: O(v+e)
        """
        # build graph
        graph = {i: [] for i in range(1, n+1)}

        for t in times:
            u, v, wt = t
            graph[u].append([v, wt])

        def dijkstras(k):
            index = k - 1
            dist = [float('inf')] * n
            dist[index] = 0
            heap = []
            heapq.heappush(heap, (0, k))

            while heap:
                dis, node = heapq.heappop(heap)

                for adj in graph[node]:
                    adj_c, adj_d = adj
                    if adj_d + dis < dist[adj_c - 1]:
                        dist[adj_c - 1] = adj_d + dis
                        heapq.heappush(heap, (dist[adj_c - 1], adj_c))

            return dist

        distances = dijkstras(k)
        if max(distances) == float('inf'):
            return -1
        else:
            return max(distances)