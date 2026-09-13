class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        profit = 0
        for i in range(1, n):
            profit = max(
                profit,
                prices[i] - min_price
            )
        
            min_price = min(
                min_price,
                prices[i]
            )
        
        return profit