class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}        
        for i,val in enumerate(nums):
            check = target - val
            if (check) in mp:
                return [mp[check],i]
            else:
                mp[val] = i