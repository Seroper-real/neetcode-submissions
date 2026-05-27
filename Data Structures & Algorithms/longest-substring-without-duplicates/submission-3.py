class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        l = 0
        win = deque()
        store = set()
        for c in s:
            while c in store:
                store.remove(win.popleft())
            win.append(c)
            store.add(c)
            l = max(l,len(win))
        return l