#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        max_m = int(math.log(n, 2))
        for m in range(max_m, 1, -1):
            k = int(n**(1 / m))
            if k**(m + 1) == n * k - n + 1:
                return str(k)
        return str(n - 1)


s = Solution()
print(s.smallestGoodBase("13"))
print(s.smallestGoodBase("4681"))
print(s.smallestGoodBase("1000000000000000000"))
