class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = defaultdict(int)
        maxl = 0

        for right in range(0, len(s)):
            freq[s[right]] += 1
            window_len = right - left + 1
            max_c = max(freq.values())
            while (window_len-max_c > k):
                freq[s[left]] -= 1
                left += 1
                window_len = right - left + 1
                max_c = max(freq.values())


            else:
                maxl = max(maxl, window_len)

        
        return maxl


