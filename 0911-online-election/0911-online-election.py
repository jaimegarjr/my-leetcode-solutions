class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons, self.times = persons, times
        self.leads, lead, counter = [], -1, defaultdict(int)
        
        for p in self.persons:
            counter[p] += 1
            if counter[p] >= counter[lead]: lead = p
            self.leads.append(lead)

    def findRecentVote(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return m
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
    
    def q(self, t: int) -> int:
        return self.leads[bisect.bisect(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)