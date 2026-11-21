class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        counts = [0] * 26
        for string in strs:
            counts = [0] * 26
            for char in string:
                counts[ord(char) - ord('a')] += 1
            
            key = tuple(counts)
            groups[key].append(string)

        return list(groups.values())

