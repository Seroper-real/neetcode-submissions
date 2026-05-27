class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        l = 0
        win = deque()
        for c in s:
            while c in win:
                win.popleft()
            win.append(c)
            l = max(l,len(win))
        return l