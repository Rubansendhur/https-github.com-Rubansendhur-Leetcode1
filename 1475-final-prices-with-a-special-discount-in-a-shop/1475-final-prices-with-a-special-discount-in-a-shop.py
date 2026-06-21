class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        low_price = 0
        res = prices[:]
        
        for i in range(0 , len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    res[i] = prices[i] - prices[j]
                    break
                else:
                    continue

            # res[i] = low_price
        
        return res