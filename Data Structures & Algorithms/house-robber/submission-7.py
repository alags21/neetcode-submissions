class Solution:
    def rob(self, nums: List[int]) -> int:
        # let T[i] be the maximum attainable value of all houses up to index i 
        n = len(nums)
        t0 = nums[0]
        t1 = 0
        # 2 choices:
        # rob the current house: T[i-2] + nums[i]
        # skip the current house: T[i-1]
        # take the max of both

        # base case - robbing house 0 is always optimal
        # base case - T[1] base = max(nums[0], nums[1])
        if n==1:
            return nums[0]
        t1 = max(nums[0], nums[1])
        for i in range(2, n):
            temp = t1
            t1 = max(t1, t0 + nums[i])
            t0 = temp
        return t1