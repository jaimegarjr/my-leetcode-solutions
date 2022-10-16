class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """
        Runtime: O(n*m + mlogm)
        Space: O(nm)
        n = number of votes
        m = number of teams (letters)
        """
        if len(votes) == 1:
            return votes[0]
        
        # keys represent the candidates
        # index of array in dict represent the rank
        # value of array item represent number of votes casted
        ranks = {}
        for v in votes:
            for i, c in enumerate(v):
                if c not in ranks:
                    ranks[c] = [0] * len(v)
                
                ranks[c][i] += 1
        
        teams = sorted(ranks.keys())
        res = sorted(teams, key=lambda x: ranks[x], reverse=True)
        return ''.join(res)