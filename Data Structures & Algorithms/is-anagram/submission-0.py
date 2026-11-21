class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scharMap = {}
        tcharMap = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if scharMap.get(s[i]):
                scharMap[s[i]] += 1
            else:
                scharMap[s[i]] = 1
            
            if tcharMap.get(t[i]):
                tcharMap[t[i]] += 1
            else:
                tcharMap[t[i]] = 1
        
        if scharMap == tcharMap:
            return True
        else:
            return False