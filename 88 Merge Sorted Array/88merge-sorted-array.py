class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end_nums1 = m - 1
        end_nums2 = n - 1

        for i in range(len(nums1) - 1, -1, -1):
            if end_nums2 < 0:
                break

            if end_nums1 > -1 and nums1[end_nums1] >= nums2[end_nums2]:
                nums1[i] = nums1[end_nums1]
                nums1[end_nums1] = 0
                end_nums1 -= 1
            else:
                nums1[i] = nums2[end_nums2]
                end_nums2 -= 1
            
        
        