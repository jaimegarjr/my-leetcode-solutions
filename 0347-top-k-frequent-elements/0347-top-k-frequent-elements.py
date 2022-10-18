class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds K most frequent numbers in input nums
        Runtime: O(nlogn)
        Space: O(n)
        """
        freq = defaultdict(int)
        res = []

        for n in nums:
            freq[n] += 1

        sortedRes = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        for i in range(k):
            res.append(sortedRes[i])

        return res