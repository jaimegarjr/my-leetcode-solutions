class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Runtime: O(nlogn)
        Space: O(n)
        """
        s = sorted(s)
        t = sorted(t)
        
        return s == t if True else False