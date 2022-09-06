class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        filtered = ""
        for c in paragraph:
            if c.isalnum():
                filtered += c.lower()
            else:
                filtered += ' '

        freqMap = collections.Counter(filtered.split())

        for key, val in freqMap.most_common():
            if key in banned:
                continue
            else:
                return key