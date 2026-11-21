class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        pref = [1] * len(nums) # product of everything up to i
        suff = [1] * len(nums) # product of everything after i
        j = len(nums) - 2
        pref[0] = 1
        suff[len(nums)-1] = 1
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
            suff[j] = suff[j+1] * nums[j+1]
            j -= 1

        for i in range(len(pref)):
            output[i] = suff[i] * pref[i]
        return output