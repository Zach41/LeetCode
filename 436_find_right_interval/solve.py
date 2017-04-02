#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bisect


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        l = sorted([(e.start, i) for (i, e) in enumerate(intervals)])
        rec = []
        for interval in intervals:
            # r = bisect.bisect_left(l, (interval.end,))
            r = self.find_right(l, interval)
            rec.append(l[r][1] if r < len(l) else -1)
        return rec

    def find_right(self, ls, interval):
        l, r = 0, len(ls) - 1
        while l < r:
            mid = l + (r-l) // 2
            if ls[mid][0] == interval.end:
                return mid
            elif ls[mid][0] < interval.end:
                l = mid + 1
            else:
                r = mid - 1
        if interval.end > ls[r][0]:
            return r + 1
        else:
            return r


s = Solution()

i1 = Interval(3, 4)
i2 = Interval(2, 3)
i3 = Interval(1, 2)
print(s.findRightInterval([i1, i2, i3]))
