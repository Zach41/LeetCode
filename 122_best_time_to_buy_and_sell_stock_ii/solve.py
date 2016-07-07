#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        n = len(prices)
        if n <= 1:
            return 0
        start = 0
        for i in range(0, n-1):
            if prices[i+1] >= prices[i]:
                continue
            else:
                max_profit += prices[i] - prices[start]
                start = i+1

        max_profit += prices[n-1] - prices[start]

        return max_profit

s = Solution()
print s.maxProfit([1, 2, 3, 4, 5, 6, 7])
print s.maxProfit([7, 1, 3, 5, 6, 4])
print s.maxProfit([7, 6, 5, 4, 3, 2, 1])
