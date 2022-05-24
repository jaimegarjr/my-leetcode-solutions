class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Runtime: O(nlogn)
        Space: O(n)
        """
        # return sorted(s) == sorted(t) if True else False
        
        """
        Runtime: O(n)
        Space: O(n) -> O(1), bcs 26 dis. chars
        """
        freq = {}
        
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        for c in t:
            if c in freq:
                freq[c] -= 1
                if freq[c] == 0:
                    del freq[c]
            else:
                return False
        
        return len(freq) == 0 if True else False