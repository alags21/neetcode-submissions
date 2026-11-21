class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        j = n - 2
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[j] = suffix[j+1] * nums[j+1]
            j -= 1
        
        res = []
        for i in range (n):
            res.append(prefix[i] * suffix[i])

        return res
