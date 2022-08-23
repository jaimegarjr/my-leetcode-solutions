class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Runtime: O(n)
        # Space: O(1)
        if not needle: return 0
        if needle not in haystack: return -1
        
        l, r = 0, len(needle) - 1
        
        while r < len(haystack):
            if haystack[l:r+1] == needle:
                break
            l += 1
            r += 1
        
        return l
        