class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1) 
    def binary_search(self, nums, target, l, r):
        if l > r:
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
            
