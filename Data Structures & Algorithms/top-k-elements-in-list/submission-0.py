class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sorted_keys = [k for k,v in sorted(freq.items(), key=lambda x: x[1])]
        return sorted_keys[len(sorted_keys)-k:]

