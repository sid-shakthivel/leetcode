class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isSufficient(capacity):
            counting_days = 1
            counting_weight = 0

            for weight in weights:
                if counting_weight + weight <= capacity:
                    counting_weight += weight
                else:
                    counting_days += 1
                    counting_weight = weight

            return counting_days <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if isSufficient(mid):
                right = mid
            else:
                left = mid + 1

        return left