#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        def count(n):
            if n == 1:
                return 10
            else:
                sum , cur = 9, 9
                n = n-1
                while n>0:
                    sum *= cur
                    cur -= 1
                    n   -= 1
                return sum

        if n <= 0:
            return 1;
        tot = 0
        for i in range(n, 0, -1):
            tot += count(i)
        return tot

s = Solution()

print s.countNumbersWithUniqueDigits(2)
print s.countNumbersWithUniqueDigits(3)
            
                    
