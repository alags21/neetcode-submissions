class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Valid = replacements + max freq >= window
        if (len(s) == 1): return 1
        L = 0
        max_freq = defaultdict(int)
        max_len = 0
        for R in range(0, len(s)):
            window_size = R-L+1
            max_freq[s[R]] += 1
            curr_max = max(max_freq.values())

            valid = (k + curr_max >= window_size)
            while not (valid) and L<=R:
                max_freq[s[L]] = max(0, max_freq[s[L]] - 1)

                L += 1
                curr_max = max(max_freq.values())
                window_size = R-L+1
                valid = (k + curr_max >= window_size)

            window_size = R-L+1
            max_len = max(max_len, window_size)
        return max_len
