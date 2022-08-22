class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Runtime: O(n)
        # Space: O(n)
        res = []
        
        for i in range(len(intervals)):
            start, end = 0, 1
            
            if newInterval[end] < intervals[i][start]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][end] < newInterval[start]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][start], newInterval[start]),
                    max(intervals[i][end], newInterval[end])
                ]
        
        res.append(newInterval)
        
        return res