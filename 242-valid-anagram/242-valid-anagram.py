class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Runtime: O(nlogn)
        Space: O(n)
        """
        return sorted(s) == sorted(t) if True else False