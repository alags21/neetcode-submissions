class Solution:
    def findMin(self, nums: List[int]) -> int:
        # i would use binary search here since we can guarantee that the array switches from increasing to decreasing at exactly one index. once we find that index, we know that the minimum is presently at that index, or to the right of it.
        L = 0
        R = len(nums) - 1
        first = nums[L]
        last = nums[R]
        while (L < R):
            mid = (L+R) // 2
            # if mid+1 element is less, we fonud min, can return mid+1
            # if mid+1 is greater than first, we know left size of array must not have any pivots
            # if mid-1 is greater, we know array increases to the right
            if (nums[mid] > nums[R]):
                L = mid+1
            else:
                R = mid
        return nums[L]