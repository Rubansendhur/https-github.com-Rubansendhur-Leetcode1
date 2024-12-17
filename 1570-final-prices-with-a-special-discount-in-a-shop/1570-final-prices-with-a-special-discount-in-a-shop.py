class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0] * len(prices)
        stack = []

        for i in range(len(prices)-1 , -1, -1):
            while len(stack) > 0 and prices[i] < stack[-1]:
                stack.pop()
            if len(stack) == 0:
                ans[i] = -1
            else:
                ans[i] = stack[-1]

            stack.append(prices[i]) 

            if (ans[i] != -1):
                prices[i] -= ans[i]          

        return prices
        
        