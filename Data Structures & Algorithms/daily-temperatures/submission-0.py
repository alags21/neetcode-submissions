class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mstack = []
        result = [0] * len(temperatures)
        mstack.append(0)
        for t in range(1, len(temperatures)):
            temp = temperatures[t]
            days = 1
            while mstack != [] and temperatures[mstack[-1]] < temp:
                result[mstack[-1]] = t-mstack[-1]
                mstack.pop()
                days += 1
            mstack.append(t)
        return result