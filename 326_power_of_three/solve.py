#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isPowerOfThree(self, n):
        s = 1

        while s <= n:
            if s == n:
                return True
            else:
                s *= 3
        return False

s = Solution()

print s.isPowerOfThree(4)
print s.isPowerOfThree(27)
