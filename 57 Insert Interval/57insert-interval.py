class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        inserted = False

        for i in range(len(intervals)):
            interval = intervals[i]

            if interval[1] < newInterval[0]:
                new_intervals.append(interval)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    new_intervals.append(newInterval)
                    
                inserted = True
                new_intervals.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        if not inserted:
            new_intervals.append(newInterval)

        return new_intervals