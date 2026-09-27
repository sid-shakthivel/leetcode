class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])
        print(sorted_points)

        interval = sorted_points[0]

        min_arrows = 0

        for i in range(1, len(sorted_points)):
            curr_interval = sorted_points[i]
            if curr_interval[0] >= interval[0] and curr_interval[0] <= interval[1]:
                interval[0] = max(interval[0], curr_interval[0])
                interval[1] = min(interval[1], curr_interval[1])
            else:
                min_arrows += 1
                interval = curr_interval

        return min_arrows + 1