class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums,target, 0, len(nums))
    
    def binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        idx = start + ((end - start) // 2)
        k = nums[idx]
        if k == target: return idx
        elif end - start == 1: return -1
        elif k < target: return self.binary_search(nums, target, idx, end)
        return self.binary_search(nums, target, start, idx)