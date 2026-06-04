class Solution:
    def minWindow(self, s: str, t: str) -> str:
        store = defaultdict(int)
        for c in t: store[c] += 1
        win = deque()
        sol = None
        for c in s:
            win.append(c)
            if c in store: store[c] -= 1
            while win and self.is_solution(store):
                #print(f"sol: {win}, {store}")
                sol = self.get_solution(sol, win)
                ch = win.popleft()
                if ch in store: store[ch] += 1
        if sol == None: return ""
        return sol

    def is_solution(self, store: dict[str,int]) -> bool:
        for v in store.values():
            if v > 0: return False
        return True

    def get_solution(self, current_sol: str|None, win: deque) -> str:
        sol = ""
        for c in win: sol+=c
        if current_sol == None or len(sol) < len(current_sol): return sol
        return current_sol




