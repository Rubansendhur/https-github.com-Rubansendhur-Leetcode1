class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        start = prices[0]
        max_profit = 0

        for i in range(1 , n):
            start = min(start, prices[i])
            max_profit = max(max_profit, abs(start - prices[i]))
        
        return max_profit