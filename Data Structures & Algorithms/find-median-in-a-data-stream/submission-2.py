class MedianFinder:

    def __init__(self):
        self.store = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.store, num)

    def findMedian(self) -> float:
        if len(self.store) == 1: return self.store[0]
        if len(self.store) == 2: return (self.store[0] + self.store[1]) / 2
        middle = len(self.store) // 2
        odd = len(self.store) % 2 == 1
        backup = []
        for _ in range(middle+1):
            backup.append(heapq.heappop(self.store))
        
        if odd: res = backup[-1]
        else: res = (backup[-1] + backup[-2]) / 2
        
        for val in backup: heapq.heappush(self.store,val)
        #print(middle, res, sorted(self.store), backup)
        return res