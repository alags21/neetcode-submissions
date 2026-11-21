class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting is O(nlogn)
        maxheap = []
        for value in nums:
            heapq.heappush(maxheap, -value)
        for i in range(k-1):
            heapq.heappop(maxheap)
        return -heapq.heappop(maxheap)

