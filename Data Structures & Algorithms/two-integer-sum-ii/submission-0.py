class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            diff = target - num
            for k in range(i,len(numbers)):
                if numbers[k] == diff: return [i+1,k+1]
                if numbers[k] > diff: break
        