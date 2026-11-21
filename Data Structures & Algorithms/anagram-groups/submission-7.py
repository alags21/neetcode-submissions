class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        base = ord('a')

        for string in strs:
            counts = [0] * 26
            for char in string:
                counts[ord(char)-base] += 1
            
            groups[tuple(counts)].append(string)
        
        return list(groups.values())