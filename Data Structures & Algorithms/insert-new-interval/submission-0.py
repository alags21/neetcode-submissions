class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            n1,n2 = newInterval

            c1,c2 = intervals[i]
            # 3 cases: 
            # new is before current interval
            if (n2 < c1):
                res.append(newInterval)
                return res + intervals[i:]

            # new is completely after
            elif (n1 > c2):
                res.append(intervals[i])
            
            else:
                newInterval = [min(n1,c1), max(n2,c2)]
        
        res.append(newInterval)
        return res