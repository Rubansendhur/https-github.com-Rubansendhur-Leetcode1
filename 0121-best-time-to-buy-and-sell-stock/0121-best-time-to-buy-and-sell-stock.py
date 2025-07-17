class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        start = prices[0]
       
        for i in range(1 , len(prices)):
            if prices[i] < start:
                start = prices[i]
            maxprofit = max(prices[i] - start, maxprofit)
        return maxprofit

            
            
            
        