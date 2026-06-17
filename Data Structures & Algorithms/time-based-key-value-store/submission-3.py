class TimeMap:

    def __init__(self):
        self.store = defaultdict(str)
        self.mx = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key+str(timestamp)] = value
        self.mx[key].append(timestamp)
 
    def get(self, key: str, timestamp: int) -> str:
        #print(f"key:{key}, ts:{timestamp}, store:{self.store}, mx:{self.mx}")
        if key in self.mx:
            ts = self.b_search(self.mx[key], timestamp, 0, len(self.mx[key])-1, -1)
            #print(f"Search for {timestamp} in {self.mx[key]}, found {ts}")
            return self.store[key+str(ts)] if ts > -1 else ""
        return ""

    def b_search(self, timestamps: List[int], target: int, l: int, r: int, mx: int) -> int:
        if l > r:
            return mx
        m = (l + r) // 2
        if timestamps[m] == target: return target
        elif timestamps[m] < target:
            mx = max(mx,timestamps[m])
            return self.b_search(timestamps, target, m+1, r, mx)
        else: return self.b_search(timestamps, target, l, m-1, mx)
