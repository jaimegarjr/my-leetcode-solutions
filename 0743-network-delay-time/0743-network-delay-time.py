class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Returns the max time to send a signal to all nodes from node k
        Runtime: O(elogv)
        Space: O(v+e)
        """
        # build graph
        visited = set()
        graph = {i: [] for i in range(1, n+1)}

        for u, v, wt in times:
            graph[u].append((v, wt))

        def dijkstrasAlgo(k):
            t = 0
            minHeap = [(0, k)]

            while minHeap:
                w1, n1 = heapq.heappop(minHeap)
                if n1 in visited:
                    continue
                visited.add(n1)
                t = max(t, w1)

                for n2, w2 in graph[n1]:
                    if n2 not in visited:
                        heapq.heappush(minHeap, (w1 + w2, n2))

            return t

        maxTime = dijkstrasAlgo(k)
        return maxTime if len(visited) == n else -1