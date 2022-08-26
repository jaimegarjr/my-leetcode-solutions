class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []
        
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in anagrams:
                anagrams[sortedS].append(s)
            else:
                anagrams[sortedS] = [s]
        
        for k, v in anagrams.items():
            res.append(v)
        
        return res