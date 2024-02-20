# Best Time to Buy and Sell Stock II
# Time: O(n) | Space: O(1)
# Mua đáy bán ở đỉnh =))
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            curPrice = prices[i+1] - prices[i]
            if curPrice > 0:
                res += curPrice
        
        return res