class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lid, rid = 0, len(numbers) - 1
        while lid < rid:
            sm = numbers[lid] + numbers[rid]
            if sm == target: return [lid+1, rid+1]
            if sm > target: rid -= 1
            else: lid +=1