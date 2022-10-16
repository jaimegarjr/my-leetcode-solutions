class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]
        
        ranks = {}
        
        for v in votes:
            for i, c in enumerate(v):
                if c not in ranks:
                    ranks[c] = [0] * len(v)
                
                ranks[c][i] += 1
        
        teams = sorted(ranks.keys())
        res = sorted(teams, key=lambda x: ranks[x], reverse=True)
        return ''.join(res)