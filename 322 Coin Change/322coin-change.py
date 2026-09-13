class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        # dp[i] represents the fewest number of coins to make i
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                min_coins = float('inf')

                for coin in coins:
                    if i - coin > 0:
                        min_coins = min(1 + dp[i - coin], min_coins)
                
                dp[i] = min_coins

        return -1 if dp[-1] == float('inf') else dp[-1] 