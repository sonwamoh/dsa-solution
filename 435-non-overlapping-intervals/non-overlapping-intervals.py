class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : (i[1], i[0]))
        overlaps = 0
        intervals_tracker = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = intervals_tracker[-1][1]
            if start < last_end:
                overlaps += 1
            else:
                intervals_tracker.append([start, end])
        return overlaps
    """
    [[1,2]]
    """