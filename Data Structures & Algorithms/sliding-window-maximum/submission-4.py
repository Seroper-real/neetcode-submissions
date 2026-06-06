class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mon = deque()
        res = []
        for i in range(k):
            self.add(mon,nums[i],i)
        res.append(mon[0][1])
        for i in range(k,len(nums)):
            #print(f"mon:{mon}")
            if mon[0][0] < i - k + 1: 
                #it means max value popping out
                mon.popleft()
            self.add(mon,nums[i],i)
            res.append(mon[0][1])
        return res

    def add(self, mon: deque, val: int, i: int):
        while mon and mon[-1][1] <= val:
            mon.pop()
        mon.append((i,val))
