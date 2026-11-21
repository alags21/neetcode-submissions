class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        while (L <= R):
            mid = (R+L)//2
            if target > nums[mid]:
                L=mid+1
            elif target<nums[mid]:
                R=mid-1
            else:
                return mid
        return -1
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
            
