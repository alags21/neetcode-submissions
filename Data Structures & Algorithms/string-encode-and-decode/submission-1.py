class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            for c in string:
                res += str(ord(c))
                res += "_"

            res += " "
        
        return res
    def decode(self, s: str) -> List[str]:
        res = [""]
        c=0
        curr = ""
        while c < len(s):
            if s[c] == " ":
                res.append("")
                
            elif s[c] == "_":
                res[-1] += chr(int(curr))
                curr = ""
            
            else:
                curr += s[c]
            
            c += 1
        return res[:-1]