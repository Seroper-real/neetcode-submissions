class Solution:
    def minWindow(self, s: str, t: str) -> str:
        store = defaultdict(int)
        for c in t: store[c] += 1
        lid, rid = 0, 0
        sol = None
        while rid < len(s):
            c = s[rid]
            if c in store: store[c] -= 1
            while self.is_solution(store):
                tmp_sol = s[lid:rid+1]
                #print(f"tmp_sol:{tmp_sol}")
                if sol == None or len(tmp_sol) < len(sol): sol = tmp_sol
                ch = s[lid]
                if ch in store: store[ch] += 1
                lid += 1
            rid += 1
        if sol == None: return ""
        return sol

    def is_solution(self, store: dict[str,int]) -> bool:
        for v in store.values():
            if v > 0: return False
        return True





