class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1) 
    def binary_search(self, nums, target, l, r):
        if (r-l) == 0:
            if (nums[l] == target):
                return l
            else:
                return -1
        if (r-l) == 1:
            if (nums[r] == target):
                return r
            elif (nums[l] == target):
                return l
            else:
                return -1
        mid = l + (r-l) // 2
        mid_n = nums[mid]
        if (mid_n==target):
            return mid
        else:
            if (mid_n > target):
                return self.binary_search(nums, target, l, mid-1)
            else:
                return self.binary_search(nums, target, mid+1, r)
            
