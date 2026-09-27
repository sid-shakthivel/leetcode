class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        rtn = [0] * len(nums)

        left = 0
        right = len(nums) - 1

        index = len(nums) - 1

        while left <= right:
            square_left = nums[left] * nums[left]
            square_right = nums[right] * nums[right]

            if square_left > square_right:
                rtn[index] = square_left
                left += 1
            else:
                rtn[index] = square_right
                right -= 1

            index -= 1

        return rtn