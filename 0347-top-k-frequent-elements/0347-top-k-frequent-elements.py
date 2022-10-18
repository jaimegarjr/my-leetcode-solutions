class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds K most frequent numbers in input nums
        Runtime: O(nlogn)
        Space: O(n)
        """
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        keys = freq.keys()
        sortedArr = sorted(keys, key=lambda x: freq[x], reverse=True)
        res = []

        for i in range(k):
            res.append(sortedArr[i])

        return res