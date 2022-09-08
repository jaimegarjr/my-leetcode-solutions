class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSub = ""

        # uneven string length pass
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r <= len(s)-1:
                subStr = s[l:r+1]
                if s[l] != s[r]:
                    break
                if len(subStr) > len(maxSub):
                    maxSub = subStr
                l -= 1
                r += 1

        # even string length pass
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r <= len(s)-1:
                subStr = s[l:r+1]
                if s[l] != s[r]:
                    break
                if len(subStr) > len(maxSub):
                    maxSub = subStr
                l -= 1
                r += 1

        return maxSub