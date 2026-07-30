class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def perm(nums: List[int], size: int, part: List[int], res: List[int]):
            if len(part) == size:
                res.append(part.copy())
                return
            if len(part) > size: return

            for i, val in enumerate(nums):
                part.append(val)
                nums.pop(i)
                perm(nums, size, part, res)
                nums.insert(i,val)
                part.pop()
        
        perm(nums, len(nums), [], res)
        return res