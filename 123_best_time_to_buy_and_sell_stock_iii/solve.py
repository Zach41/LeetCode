#!/usr/bin/env python
# -*- coding : utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        
        max_left = [0] * n
        max_right = [0] * n
        min_p = prices[0]

        for i in range(1, n):
            max_left[i] = max(prices[i] - min_p, max_left[i-1])
            if min_p > prices[i]:
                min_p = prices[i]

        max_p = prices[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_p - prices[i], max_right[i+1])
            if prices[i] > max_p:
                max_p = prices[i]
                
        max_ans = 0
        for i in range(n):
            if max_ans < max_left[i] + max_right[i]:
                max_ans = max_left[i] + max_right[i]
        return max_ans

s = Solution()
print s.maxProfit([1, 2, 3, 4, 5, 6, 7])
import pdb
pdb.set_trace()
print s.maxProfit([0, 2, 1, 2, 7, 0, 8])
print s.maxProfit([1, 1, 1, 1])
print s.maxProfit([4, 3, 2, 1])
            

