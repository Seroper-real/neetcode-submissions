class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(sorted(candidates), target, 0, 0, [], res)
        return res

    def dfs(self, candidates: List[int], target: int, idx: int, partial_sum: int, partial: List[int], res: List[int]):
        if partial_sum == target:
            res.append(partial.copy())
            return
        if idx >= len(candidates) or partial_sum > target: return
        

        item = candidates[idx]
        partial.append(item)
        self.dfs(candidates, target, idx + 1, partial_sum + item, partial, res)
        partial.pop()

        skip_idx = idx
        while skip_idx < len(candidates) and candidates[skip_idx] == candidates[idx]:
            skip_idx += 1
        self.dfs(candidates, target, skip_idx, partial_sum, partial, res)