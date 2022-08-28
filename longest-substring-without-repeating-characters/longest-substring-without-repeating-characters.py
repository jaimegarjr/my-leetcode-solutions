class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freqMap = {}
        start = res = 0
        
        for end in range(len(s)):
            c = s[end]
            if c not in freqMap:
                freqMap[c] = 1
                res = max(res, end - start + 1)
            else:
                freqMap[c] += 1
                while freqMap[c] > 1:
                    freqMap[s[start]] -= 1
                    if freqMap[s[start]] == 0:
                        del freqMap[s[start]]
                    start += 1
            
        return res