#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            mid_cal = self._cal(mid)
            if mid_cal == n:
                return mid
            elif mid_cal < n:
                l = mid + 1
            else:
                r = mid - 1
        if n >= self._cal(l):
            return l
        else:
            return l-1

    def _cal(self, n):
        return (n * n + n) // 2


s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
print(s.arrangeCoins(6))
