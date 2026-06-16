class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.b_search(nums, 0, len(nums) - 1, nums[0])
    
    def b_search(self, nums: List[int], lid: int, rid: int, mn: int) -> int:
        if lid > rid: return mn
        mid = (rid + lid) // 2
        mn = min(mn, nums[mid])
        #print(f"lid:{nums[lid]}, rid:{nums[rid]}, mid:{nums[mid]}")
        if nums[lid] < nums[rid] or nums[mid] < nums[rid]:
            return self.b_search(nums, lid, mid - 1, mn)
        else:
            return self.b_search(nums, mid + 1, rid, mn)