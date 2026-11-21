class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        intfreq = defaultdict(int)

        for num in nums:
            intfreq[num] += 1
        
        int_freqs = intfreq.items()
        sorted_ints = sorted(int_freqs, key=lambda f : f[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_ints[i][0])
        
        return res
