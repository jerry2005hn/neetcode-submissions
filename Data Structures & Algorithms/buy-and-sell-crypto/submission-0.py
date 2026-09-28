class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                buy = prices[i]
                sell = prices[j]
                profit = sell - buy
                res = max(profit,res)
        return res