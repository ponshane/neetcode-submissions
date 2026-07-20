class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentMin = prices[0]

        for i in range(1, len(prices)):
            if currentMin > prices[i]:
                currentMin = prices[i]
            else:
                profit = prices[i] - currentMin
                maxProfit = max(maxProfit, profit)
        return maxProfit
