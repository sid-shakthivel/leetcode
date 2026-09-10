class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            
            frequencies[num] += 1

        heap = []

        for key, value in frequencies.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)

        return [unit[1] for unit in heap]