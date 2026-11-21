class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {']': '[', ')': '(', '}':'{'}
        for char in s:
            if char in '({[':
                stack.append(char)
                continue
            else:
                if stack==[]:
                    return False
                if stack[-1]==matches[char]:
                    stack.pop()
                else:
                    return False
        return (stack==[])
