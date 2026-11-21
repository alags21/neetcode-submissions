class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # since all weights are positive, we can use dijsktras to find the shortest path 
        # i need to convert times to an adjacency list
        graph = {node: [] for node in range(1,n+1)}
        # time = (ui source, vi target, ti = edge cost)
        # graph = {ui: (target, cost)}
        for time in times:
            graph[time[0]].append((time[1], time[2]))

        #now for djikstras: need a distance map and a preiority queue/minheap

        dist = {node: float('inf') for node in range(1,n+1)}
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            # get current node
            d, node = heapq.heappop(pq)
            # skip the outdated entires (d in pq is greater than stored distance)
            if d > dist[node]:
                continue
            for nei, w in graph[node]:
                new_dist = d+w
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(pq, (new_dist, nei))
        
        time = float(0)
        for node in dist:
            if dist[node]==float('inf'):
                return -1
            else:
                time = max(time, dist[node])
        return time
        