class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.comb(nums, target, 0, [], res, 0)
        return res

    def comb(self, nums: List[int], target:int, partial_sum: int, partial: List[int], res: List[int], idx : int):
        if partial_sum == target:
            res.append(partial.copy())
            return
        if idx >= len(nums) or partial_sum > target:
            return
        
        partial.append(nums[idx])
        self.comb(nums, target, partial_sum + nums[idx], partial, res, idx)
        partial.pop()
        self.comb(nums, target, partial_sum, partial, res, idx+1)
