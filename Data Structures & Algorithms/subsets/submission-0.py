class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.subset(nums, 0, [], res)
        return res

    def subset(self, nums: List[int], idx: int, partial: List[int], res: List[int]) -> None:
        if idx == len(nums):
            res.append(list(partial))
            return
        _partial = list(partial)
        self.subset(nums, idx + 1, partial, res) #Not adding number
        _partial.append(nums[idx])
        self.subset(nums, idx + 1, _partial, res)

    
