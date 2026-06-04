class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store1 = defaultdict(int)
        for c in s1: store1[c] += 1
        win = deque()
        store2 = defaultdict(int)
        for c in s2:
            win.append(c)
            store2[c] += 1
            if len(win) > len(s1):
                ch = win.popleft()
                store2[ch] -= 1
            found = True
            for k,val in store1.items():
                if k not in store2 or store2[k] != val:
                    found = False
                    break
            if found: return True
        return False