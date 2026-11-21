class Solution:
    def rob(self, nums: List[int]) -> int:
        # let T[i] be the maximum attainable value of all houses up to index i 
        n = len(nums)
        T = [0 for i in range(n)]

        # 2 choices:
        # rob the current house: T[i-2] + nums[i]
        # skip the current house: T[i-1]
        # take the max of both

        # base case - robbing house 0 is always optimal
        T[0] = nums[0]
        for i in range(1, n):
            T[i] = max(T[i-1], T[i-2] + nums[i])

        return T[n-1]