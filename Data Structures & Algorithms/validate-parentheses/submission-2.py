class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(':')','[':']','{':'}'}
        for c in s:
            if c in pair.keys():
                stack.append(c)
            else: 
                if not stack: return False
                ch = stack.pop()
                if pair[ch] != c: return False
        return len(stack) == 0