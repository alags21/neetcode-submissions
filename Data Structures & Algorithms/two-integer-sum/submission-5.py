class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {} # num, index
        for i in range(len(nums)):
            need = target - nums[i]
            if need in found:
                return [found[need], i]
            else:
                found[nums[i]] = i

        return