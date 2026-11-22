class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # since we can step to either step i+1 or i+2, 
        # dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        # start at index 0
        # dp[0] is 0 since we start there
        # dp[1] is cost of stepping from floor 0 since we start there
        # dp[i] is the minimum cost of reaching step i
        dp = [0] * (len(cost)+1)

        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        print(dp)
        return dp[len(cost)]