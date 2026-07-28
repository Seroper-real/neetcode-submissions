class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.comb(nums, target, 0, [], res, 0)
        return res

    def comb(self, nums: List[int], target:int, partial_sum: int, partial: List[int], res: List[int], idx : int):
        #print(partial, idx)
        if partial_sum == target:
            res.append(partial.copy())
            return
        if idx >= len(nums) or partial_sum > target:
            return
        
        #This branch actually add the next number to the partial
        partial.append(nums[idx])
        self.comb(nums, target, partial_sum + nums[idx], partial, res, idx) #Responsible for adding a new number
        partial.pop()
        
        #This branch only shift the next number, this cause to see multiple time the same "partial"
        #because this branch doesn't 'update' the tree, just mimic the for loop with recursion
        self.comb(nums, target, partial_sum, partial, res, idx+1) #Responsible for shifting the index
        
