class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for [x,y] in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(minheap, (dist, [x,y]))
        ans = []
        while k > 0:
            curr = heapq.heappop(minheap)
            ans.append(curr[1])
            k -= 1
            
        return ans