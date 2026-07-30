class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def perm(used: set(int), part: List[int]):
            if len(part) == len(nums):
                res.append(part.copy())
                return

            for i, val in enumerate(nums):
                if val not in used:
                    used.add(val)
                    part.append(val)
                    perm(used,part)
                    part.pop()
                    used.remove(val)
        
        perm(set(),[])
        return res