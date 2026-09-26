

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        max_fruit_picked = 0

        fruit_types = {}

        for right in range(len(fruits)):
            fruit_types[fruits[right]] = right

            if len(fruit_types) > 2:
                oldest_fruit = min(fruit_types, key=fruit_types.get)

                left = fruit_types[oldest_fruit] + 1
                del fruit_types[oldest_fruit]

            max_fruit_picked = max(max_fruit_picked, right - left + 1)
        
        return max_fruit_picked
