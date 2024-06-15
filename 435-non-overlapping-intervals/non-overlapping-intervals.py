class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : (i[1], i[0]))
        overlaps = 0
        last_end = intervals[0]
        for start, end in intervals[1:]:
            if start < last_end[1]:
                overlaps += 1
            else:
                last_end = [start, end]
        return overlaps
    """
    [[1,2]]
    """