class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach
        curr_characters = {}

        if (s == ""):
            return 0

        if (len(s)==1):
            return 1
        
        L=0
        R=1
        curr_max = 0
        curr_characters[s[L]] = 0
        while (R <= len(s) - 1):
            right_character = s[R]
            # check if its in the dictionary
            if right_character in curr_characters:
                prev = curr_characters[right_character]
                while L <= prev:
                    curr_characters.pop(s[L])
                    L += 1

            curr_characters[right_character] = R
            curr_max = max(R - L + 1, curr_max)

            R += 1
        
        return curr_max
