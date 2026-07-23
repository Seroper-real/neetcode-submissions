class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a, b = -heapq.heappop(heap), -heapq.heappop(heap)
            c = abs(a-b)
            if c > 0: heapq.heappush(heap, -c)
        return -heap[0] if len(heap) > 0 else 0
