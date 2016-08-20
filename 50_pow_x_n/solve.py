#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def myPow(self, x, n):
        flag = True if n < 0 else False
        n = abs(n)
        base = x
        ans  = 1.0
        while n:
            if n % 2 == 1:
                ans *= base

            base = base * base
            n = n/2

        if flag:
            return 1.0 / ans
        else:
            return ans

s = Solution()
print s.myPow(1.2, 2)
print s.myPow(3, 4)
print s.myPow(2, -3)
