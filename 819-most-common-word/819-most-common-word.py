class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        filtered = ''

        for c in paragraph:
            if c.isalnum():
                filtered += c.lower()
            else:
                filtered += ' '

        freqMap = collections.Counter(filtered.split())

        for word, freq in freqMap.most_common():
            if word in banned:
                continue
            else:
                return word