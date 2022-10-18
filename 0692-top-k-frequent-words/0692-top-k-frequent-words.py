class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Runtime: O(nlogn)
        Space: O(n)
        """
        freq = collections.Counter(words)
        sortedRes = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        return sortedRes[:k]