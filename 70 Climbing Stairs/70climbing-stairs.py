class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        memo[1] = 1

        if n > 1:
            memo[2] = 2

        def recurse(num):
            if memo[num] != 0:
                return memo[num]
            else:
                memo[num] = recurse(num - 1) + recurse(num - 2)
                return memo[num]

        return recurse(n)