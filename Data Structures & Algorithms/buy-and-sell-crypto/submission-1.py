class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        money = 0
        for i,num in enumerate(prices):
            if i == 0: continue

            if num - best_buy > money:
                money = num - best_buy
            elif num < best_buy:
                best_buy = num

        return money