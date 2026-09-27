class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        rtn = 0

        interval = sorted_intervals[0]

        for i in range(1, len(sorted_intervals)):
            current_interval = sorted_intervals[i]

            if current_interval[0] < interval[1]:
                rtn += 1
            else:
                interval = current_interval

        return rtn