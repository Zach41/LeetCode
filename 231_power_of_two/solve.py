#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        p = int(math.log10(n) / math.log10(2))
        if 2**p == n:
            return True
        else:
            return False

s = Solution()

print s.isPowerOfTwo(4)
print s.isPowerOfTwo(6)
