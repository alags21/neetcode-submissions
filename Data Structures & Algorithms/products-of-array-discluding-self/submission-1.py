class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums))
        suffix = [1] * (len(nums))
        j = len(nums) - 2
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[j] = suffix[j+1] * nums[j+1]
            j -= 1
        
        res = []
        for i in range (len(nums)):
            res.append(prefix[i] * suffix[i])

        return res
