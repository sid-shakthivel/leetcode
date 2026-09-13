class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum must be to the right of mid
                left = mid + 1
            else:
                # Minimum is either mid or to the left of mid
                right = mid


        return nums[left]