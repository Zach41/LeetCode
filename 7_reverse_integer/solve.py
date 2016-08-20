#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def reverse(self, num):
        flag = True if num < 0 else False

        num = abs(num)
        digits = []
        while num:
            digits.append(num % 10)
            num /= 10
        ret = 0
        base = 1
        digits.reverse()
        for x in digits:
            ret += base * x
            base *= 10
        if flag:
            ret *= -1

        if ret > (2**31) - 1 or ret < -2**31:
            return 0
        return ret

    def reverse2(self, x):
        flag = True if x < 0 else False

        x = abs(x)
        ret = 0
        base = 1
        for c in str(x):
            ret += base * int(c)
            base *= 10
        if flag:
            ret *= -1
        if ret > (2**31-1) or ret < -2**31:
            return 0
        return ret

s = Solution()

print s.reverse2(10)
print s.reverse2(-10)
print s.reverse2(112)
        
