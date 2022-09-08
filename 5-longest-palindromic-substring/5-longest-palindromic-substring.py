class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSub = ""

        for i in range(len(s)):
            # uneven string length pass
            l = r = i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                subStr = s[l:r+1]
                if len(subStr) > len(maxSub):
                    maxSub = subStr
                l -= 1
                r += 1

            # even length pass
            l, r = i, i + 1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                subStr = s[l:r+1]
                if len(subStr) > len(maxSub):
                    maxSub = subStr
                l -= 1
                r += 1

        return maxSub