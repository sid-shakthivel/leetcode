class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        min_boats = 0

        people.sort()

        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            min_boats += 1
            right -= 1

        return min_boats