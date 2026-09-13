
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        reds = 0
        whites = 0
        blues = 0

        for num in nums:
            if num == 0:
                reds += 1
            elif num == 1:
                whites += 1
            else:
                blues += 1

        index = 0

        for _ in range(reds):
            nums[index] = 0
            index += 1

        for _ in range(whites):
            nums[index] = 1
            index += 1

        for _ in range(blues):
            nums[index] = 2
            index += 1
        


        