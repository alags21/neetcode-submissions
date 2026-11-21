class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for i in nums:
            freqs[i] += 1
        
        heap = []
        for num in freqs:
            heapq.heappush(heap, (-freqs[num], num))
        
        res = []
        while len(res) < k:
            res.append((heapq.heappop(heap)[1]))

        return res