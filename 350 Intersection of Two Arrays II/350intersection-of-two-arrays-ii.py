from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        hash_a = defaultdict(int)
        hash_b = defaultdict(int)

        for num in nums1:
            hash_a[num] += 1

        for num in nums2:
            hash_b[num] += 1

        for key, val in hash_a.items():
            if key in hash_b:
                res += [key] * min(val, hash_b[key])

        return res

        