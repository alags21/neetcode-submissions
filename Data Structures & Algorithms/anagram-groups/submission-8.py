class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # since alphabet is fixed size of 26
        # make an array with size 26, where each index represents frequency of that character in the string
        freq_maps = {}
        for string in strs:
            curr_freq = [0] * 26
            for i in range(len(string)):
                curr_freq[ord(string[i]) - ord('a')] += 1
            
            curr_freq = tuple(curr_freq)
            if curr_freq in freq_maps:
                freq_maps[curr_freq].append(string)
            else:
                freq_maps[curr_freq] = [string]

        result = []
        for freq in freq_maps:
            result.append(freq_maps[freq])

        return result