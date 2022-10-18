class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        freq = [[] for i in range(len(words) + 1)]
        
        for w in words:
            count[w] = 1 + count.get(w, 0)
        
        for w, c in count.items():
            freq[c].append(w)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for w in sorted(freq[i]):
                res.append(w)
                if len(res) == k:
                    return res