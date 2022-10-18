class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the longest substring in a string with no repeating characters
        Runtime: O(n)
        Space: O(26) = O(1)
        """
        start, res = 0, 0
        freq = {}

        for end in range(len(s)):
            c = s[end]
            if c in freq:
                freq[c] += 1
                while freq[c] != 1:
                    oldChar = s[start]
                    freq[oldChar] -= 1
                    start += 1
            else:
                freq[c] = 1

            res = max(res, end - start + 1)

        return res