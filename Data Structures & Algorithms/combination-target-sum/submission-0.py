class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.comb(nums, target, 0, [], res)
        return res

    def comb(self, nums: List[int], target:int, partial_sum: int, partial: List[int], res: List[int]):
        if partial_sum == target:
            partial_sorted = sorted(partial)
            if partial_sorted not in res: res.append(partial_sorted)
            return
        if partial_sum > target:
            return
        
        for num in nums:
            partial.append(num)
            self.comb(nums, target, partial_sum+num, partial, res)
            partial.pop()