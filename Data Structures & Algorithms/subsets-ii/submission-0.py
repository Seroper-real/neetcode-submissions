class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        partial = []
        def dfs(idx: int):
            if idx >= len(nums):
                res.append(partial.copy())
                return
            
            partial.append(nums[idx])
            dfs(idx + 1)
            partial.pop()

            idx_new = idx
            while idx_new < len(nums) and nums[idx_new] == nums[idx]: idx_new += 1

            dfs(idx_new)

        dfs(0)
        return res