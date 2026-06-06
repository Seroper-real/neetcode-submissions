class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            else: 
                if not stack: return False
                ch = stack.pop()
                if c == ')' and ch != '(': return False
                if c == ']' and ch != '[': return False
                if c == '}' and ch != '{': return False
        return len(stack) == 0