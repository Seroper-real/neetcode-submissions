class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = deque()
        counters = defaultdict(int)
        sol = 0
        for c in s:
            window.append(c)
            counters[c] += 1
            while self.calc_k(counters) > k:
                lc = window.popleft()
                counters[lc] -= 1
            sol = max(sol, len(window))
        return sol

    def calc_k(self, counters: dict[str, int]) -> int:
        mx = 0
        count = 0
        for val in counters.values():
            mx = max(mx,val)
            count += val
        return count - mx