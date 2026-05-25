class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set()
        for num in nums:
            vals.add(num)
        starters = []
        for num in nums:
            if num - 1 not in vals:
                starters.append(num)
        max_seq = 0
        seq = 0
        for num in starters:
            while num in vals:
               seq +=1
               num+=1
            max_seq = max(max_seq, seq) 
            seq = 0
        return max_seq