class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Runtime: O(nlogn)
        Space: O(n)
        """
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        count, res = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(count, res)

        return res