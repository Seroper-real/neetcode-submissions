class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mid = 0
        res = []
        for i in range(k):
            if nums[i] >= nums[mid]: mid = i #find max in first window
        res.append(nums[mid])
        for i in range(k,len(nums)):
            if nums[i] > nums[mid]:
                #new entry is the new max
                mid = i
            elif i - k + 1 > mid:
                #max is been popped out, find a new max
                tmp = mid+1
                mid = i #assume max is the last value, just to avoid None check
                for j in range(tmp,i+1):
                    if nums[j] >= nums[mid]: mid = j
            #else: pass max is not been popped out
            res.append(nums[mid])
        return res
