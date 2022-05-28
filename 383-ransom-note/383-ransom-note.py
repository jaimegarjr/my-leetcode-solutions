class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Runtime: O(n + m), where n is len(magazine) and m is len(ransomNote)
        Space: O(n), where n is len(magazine)
        """
        freq = {}
        
        for c in magazine:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        
        for c in ransomNote:
            if c in freq:
                freq[c] -= 1
                if freq[c] == 0:
                    del freq[c]
            else:
                return False
        
        return True