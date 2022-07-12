class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Runtime: O(nlogn)
        Space: O(n)
        """
        if not intervals: return True
        
        intervals = sorted(intervals, key=lambda x: x[0])
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            beg = intervals[i][0]
            if beg < end:
                return False
            else:
                end = intervals[i][1]
        
        return True
    