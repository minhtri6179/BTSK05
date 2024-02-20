# Best Time to Buy and Sell Stock
# O(n) time | O(1) space
# prices = [7,1,5,3,6,4]
# maxProfit = 5
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        for r in range(len(prices)):
            curProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, curProfit)
            if curProfit < 0:
                l = r
        return maxProfit