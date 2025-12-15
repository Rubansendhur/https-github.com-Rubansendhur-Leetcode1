class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < start:
                start = price
            else:
                max_profit = max(max_profit , price - start)
                
        return max_profit

        # if len(prices) < 2:
        #     return 0

        # for i in range (1 , len(prices)):
        #     if prices[i] < start:
        #         print(prices[i])
        #         start = prices[i]
            
        #     if prices[i+1] > start:
        #         profit = abs(start - prices[i+1])
        #         print(profit)
        #         max_profit = max(max_profit , profit)
        #         #print(max_profit)
        #     else:
        #         return 0
        
        # return max_profit
        
            
            
            
        