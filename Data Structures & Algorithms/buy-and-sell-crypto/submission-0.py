class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit_tmp = prices[i] - min_price
                if profit_tmp > profit:
                    profit = profit_tmp
        
        return profit