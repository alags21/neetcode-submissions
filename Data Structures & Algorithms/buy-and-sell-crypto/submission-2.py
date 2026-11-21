class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0
        max_prof = 0

        for R in range(len(prices)):
            LP = prices[L]
            RP = prices[R]
            if LP > RP:
                L = R
            
            max_prof = max(max_prof, RP-LP)

        return max_prof