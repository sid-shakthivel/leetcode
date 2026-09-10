class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums)

        left = 0
        num_sum = 0

        found_subarray = False

        for right in range(len(nums)):
            num_sum += nums[right]

            while num_sum - nums[left] >= target:
                num_sum -= nums[left]
                left += 1

            if num_sum >= target:
                found_subarray = True
                min_length = min(min_length, right - left + 1)

        return min_length if found_subarray else 0