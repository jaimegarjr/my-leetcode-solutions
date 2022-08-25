class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqMap = {}
            
        for i in range(len(s)):
            if s[i] not in freqMap:
                freqMap[s[i]] = [i, 1]
            else:
                freqMap[s[i]][1] += 1
        
        for key, val in freqMap.items():
            if val[1] > 1:
                continue
            else: return val[0]
        
        return -1