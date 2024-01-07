class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        currMin = float('inf')
        for price in prices:
            currMin = min(currMin, price)
            profit = price - currMin
            max_profit = max(max_profit, profit)
        return max_profit

