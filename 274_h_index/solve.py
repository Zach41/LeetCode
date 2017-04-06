#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from bisect import bisect_left


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in range(0, n):
            if citations[i] >= n - i:
                return n - i
        return 0


s = Solution()

print(s.hIndex([1]))
print(s.hIndex([100]))
print(s.hIndex([3, 0, 6, 1, 5]))
