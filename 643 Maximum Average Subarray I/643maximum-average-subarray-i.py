class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_size = k

        sum = 0
        for i in range(window_size):
            sum += nums[i]

        max_avg_val = sum

        for right in range(window_size, len(nums)):
            sum += nums[right]
            sum -= nums[right - window_size]

            max_avg_val = max(max_avg_val, sum)

        return max_avg_val / window_size