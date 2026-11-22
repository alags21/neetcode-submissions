class Solution:
    def climbStairs(self, n: int) -> int:
        # brute force - backtrack from the top step going down 1 and 2 places with recursion until you get to the bottom, then sum together number of all  the calls in the stack
        dp = [1] * (n+1)
        # dp[i] = number of ways to reach step i
        # start - base = step 1, 2
        dp[1] = 1
        # current position equals dp[i-1] + dp[i-2], sum because trying to find total possibilities
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
