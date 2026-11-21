class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        curr_len = 0
        max_len = 0
        for num in nums:
            if num-1 in numset:
                continue
            else:
                curr = num + 1
                curr_len = 1
                while curr in numset:
                    curr_len += 1
                    curr += 1
                max_len = max(curr_len, max_len)
        return max_len