class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Runtime: O(nlogn)
        Space: O(n or 1)
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        res = 0
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval[0] < end:
                res += 1
                end = min(end, interval[1])
                
            else:
                end = interval[1]
        
        return res
                