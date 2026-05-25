class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mx = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else: mx *= num
        if zeros > 1: return [0] * len(nums)
        if zeros == 1:
            res = []
            for val in nums:
                res.append(0 if val != 0 else mx)
            return res
        return [mx // n for n in nums if n != 0]