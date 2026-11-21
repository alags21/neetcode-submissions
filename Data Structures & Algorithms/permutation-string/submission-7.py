class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create frequency map of all chars in s1
        # sliding approach for s2 - keep updating frequency map of characters in s2 within the current window/substring we are checking
        # window valid when any of the frequencies in s2 map do not exceed corresponding character frequency in s1
        # when frequencies exceed, shrink
        # in each window - check if its valid - if not srhink
        # if it is valid - check if the frequency maps are equal

        s1f = defaultdict(int)
        for char in s1:
            s1f[char] += 1

        L=0
        s2f = defaultdict(int)

        for R in range(0, len(s2)):
            s2f[s2[R]] += 1
            char = s2[L]
            while s1f[char] < s2f[char] and L<R:
                L += 1
                s2f[s2[L-1]] -= 1
                if (s2f[char]==0):
                    s2f.pop(char)
                if (s1f[char]==0):
                    s1f.pop(char)
                char = s2[L]
            if s1f == s2f:
                return True
        
        return False
