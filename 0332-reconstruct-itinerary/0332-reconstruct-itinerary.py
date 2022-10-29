class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
    Reconstructs an itinerary from a given tickets list
        Runtime: O(e^2)
        Space: O(e)
        """
        graph = collections.defaultdict(list)
        tickets.sort()  # so in lexigraphical order

        # build graph
        for u, v in tickets:
            graph[u].append(v)

        res = ["JFK"]
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if node not in graph:
                return False
            
            temp = list(graph[node])
            for i, nei in enumerate(temp):
                res.append(nei)
                graph[node].pop(i)
                if dfs(nei):
                    return True
                res.pop()
                graph[node].insert(i, nei)

            return False

        dfs("JFK")
        return res