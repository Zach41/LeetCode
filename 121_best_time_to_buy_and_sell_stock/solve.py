#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for p in prices:
            max_profit = max(max_profit, p-min_price)
            if p < min_price:
                min_price = p
        return max_profit

s = Solution()
print s.maxProfit([1, 2])
print s.maxProfit([7, 6, 5, 4, 3, 2, 1])
print s.maxProfit([7, 1, 5, 3, 6, 4])
