class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        max_f = 0
        for num in nums:
            if num in freq:
                freq[num] += 1
                max_f = max(max_f, freq[num])
            else:
                freq[num] = 1
                max_f = max(max_f, freq[num])
        
        freq_list = [[] for _ in range(max_f)]
        for val,freq in freq.items():
            freq_list[freq - 1].append(val)

        result = []
        idx = len(freq_list) - 1
        while len(result) < k:
            for el in freq_list[idx]:
                result.append(el)
                if len(result) == k: return result
            idx -= 1
        return result


