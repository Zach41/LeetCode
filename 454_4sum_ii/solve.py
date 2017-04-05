#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        rec = {}
        for val1 in A:
            for val2 in B:
                rec[val1 + val2] = rec.get(val1 + val2, 0) + 1
        ans = 0
        for val1 in C:
            for val2 in D:
                if (-val1 - val2) in rec:
                    ans += rec.get(-val1 - val2)
        return ans

    def fourSumCount2(self, A, B, C, D):
        # elegant one
        AB = Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)


s = Solution()
print(s.fourSumCount2([1, 2], [-2, -1], [-1, 2], [0, 2]))
print(s.fourSumCount2([-1, -1], [-1, 1], [-1, 1], [1, -1]))
