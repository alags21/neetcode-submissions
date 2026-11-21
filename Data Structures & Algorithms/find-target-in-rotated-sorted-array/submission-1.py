class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while (L<R):
            mid = (R+L) // 2
            if (nums[mid]>nums[R]):
                L = mid + 1
            else:
                R = mid
        
        n = len(nums)
        pivot = L
        L=0
        R=n-1
        while (L<=R):
            mid = ((R + L) // 2)
            mid_a = (pivot+mid) % n
            if (nums[mid_a] == target):
                return mid_a
            elif (nums[mid_a] > target):
                R = mid -1
            else:
                L = mid+1
        return -1
