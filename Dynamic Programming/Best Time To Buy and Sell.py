class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = (2**31)-1
        for i in range(0,len(prices)):
            if(prices[i]<min_price):
                min_price = prices[i]
            if(prices[i] - min_price>max_profit):
                max_profit = prices[i]- min_price
        return max_profit
                
        