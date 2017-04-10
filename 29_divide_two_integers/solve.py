#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 2147483647
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


s = Solution()
print(s.divide(12, 5))
print(s.divide(12, 6))
print(s.divide(112312, 34))
print(s.divide(-1, 1))
print(s.divide(12, 0))
