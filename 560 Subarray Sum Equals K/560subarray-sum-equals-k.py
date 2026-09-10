class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = [0] * len(nums)

        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefix_sum[i] = prefix

        seen = defaultdict(int)
        seen[0] = 1

        for i in range(len(nums)):
            diff = prefix_sum[i] - k

            if diff in seen:
                res += seen[diff]
            
            seen[prefix_sum[i]] += 1

        return res