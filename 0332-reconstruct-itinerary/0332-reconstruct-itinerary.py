class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Reconstructs an itinerary from a given tickets list
        Runtime: O(e^2)
        Space: O(e)
        """
        tickets.sort()  # sort in lexigraphical order
        graph = {u: [] for u, v in tickets}

        # build graph
        for u, v in tickets:
            graph[u].append(v)

        def dfs(node):
            # we have found a solution
            if len(res) == len(tickets) + 1:
                return True

            # no way to get back, backtrack
            if node not in graph:
                return False

            # to avoid modifying list directly
            temp = list(graph[node])
            for i, nei in enumerate(temp):
                res.append(nei)
                graph[node].pop(i)

                if dfs(nei):
                    return True

                res.pop()
                graph[node].insert(i, nei)

            return False

        res = ["JFK"]
        dfs("JFK")
        return res