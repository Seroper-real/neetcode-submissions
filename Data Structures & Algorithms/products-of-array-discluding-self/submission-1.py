class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        prefix  = [1] * len(nums)
        postfix = [1] * len(nums)
        
        pref = 1
        for i in range(len(nums)-1):
            pref *= nums[i]
            prefix[i+1] = pref

        post = 1
        for i in range(len(nums)-1,0,-1):
            post *= nums[i]
            postfix[i-1] = post

        for i in range(len(nums)):
            result[i] = prefix[i]*postfix[i]
        return result