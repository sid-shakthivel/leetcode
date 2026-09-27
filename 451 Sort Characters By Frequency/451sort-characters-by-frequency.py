from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = defaultdict(int)
        queue = []

        for letter in s:
            frequencies[letter] += 1

        for key, value in frequencies.items():
            heapq.heappush(queue, (-value, key))

        rtn = []

        while queue:
            frequency, letter = heapq.heappop(queue)

            rtn.append(letter * -frequency)

        return "".join(rtn)

        