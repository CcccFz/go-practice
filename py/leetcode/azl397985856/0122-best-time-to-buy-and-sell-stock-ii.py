# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# https://github.com/azl397985856/leetcode/blob/master/problems/122.best-time-to-buy-and-sell-stock-ii.md


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum([prices[i] - prices[i-1] for i in range(1, len(prices)) if prices[i] > prices[i-1]])
