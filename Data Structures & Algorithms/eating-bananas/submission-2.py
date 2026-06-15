class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = 0
        #The worst solution is the max value in array => time will be len of array
        for pile in piles: mx = max(mx,pile)
        return self.b_search(piles, h, 1, mx, mx)
    

    def calculate(self, piles: List[int], h: int, k: int) -> int:
        count = 0
        for pile in piles:
            count += (pile // k)
            if pile % k > 0: count += 1
        #print(f"k:{k},count:{count},piles:{piles}")
        return count

    def b_search(self, piles: List[int], h: int, mn: int, mx: int, best: int) -> int:
        if mx == mn or mn + 1 == mx:
            time = self.calculate(piles, h, mn)
            if time <= h: best= min(best,mn)
            time = self.calculate(piles, h, mx)
            if time <= h: best= min(best,mx)
            return best
        mi = (mn + mx) // 2
        time = self.calculate(piles, h, mi)
        if time <= h:
            #Is a solution, check between this and half lower
            best = min(mi,best)
            return self.b_search(piles, h, mn, mi, best)
        else:
            #No solution found, k is too small.
            #Check between k and max
            return self.b_search(piles, h, mi, mx, best)

