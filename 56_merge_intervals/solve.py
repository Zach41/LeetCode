#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "%d - %d" % (self.start, self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n <= 1:
            return intervals
        
        cmpInterval = lambda x, y : cmp(x.start, y.start)
        intervals.sort(cmp=cmpInterval)
        ans = [intervals[0]]
        for i in range(1, n):
            if intervals[i].start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, intervals[i].end)
            else:
                ans.append(intervals[i])

        # for obj in ans:
        #     print obj

        return ans

s = Solution()
test1 = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
test2 = [Interval(1, 6), Interval(2, 3), Interval(4, 9)]
import pdb
pdb.set_trace()
print s.merge(test1)
print s.merge(test2)
