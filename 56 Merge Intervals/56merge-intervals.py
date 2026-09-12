class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = list(sorted(intervals, key = lambda x:x[0]))
        res = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            interval = sorted_intervals[i]
            last_interval = res[-1]

            if interval[0] >= last_interval[0] and interval[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], interval[1])
            else:
                res.append(interval)

        return res
            

