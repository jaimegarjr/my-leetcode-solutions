class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in anagrams:
                anagrams[sortedStr].append(s)
            else:
                anagrams[sortedStr] = [s]

        return anagrams.values()