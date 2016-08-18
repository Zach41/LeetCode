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
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        hasInsert = False
        ans = []
        for obj in intervals:
            if hasInsert:
                ans.append(obj)
                continue
            if newInterval.end < obj.start:
                ans.append(newInterval)
                hasInsert = True
                ans.append(obj)
            elif newInterval.start > obj.end:
                ans.append(obj)
            else:
                newInterval.start = min(obj.start, newInterval.start)
                newInterval.end   = max(obj.end, newInterval.end)
        if not hasInsert:
            ans.append(newInterval)
        
        for obj in ans:
            print obj
            
        return ans 
        
s = Solution()

test1 = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10),
         Interval(12, 16)]
test2 = [Interval(1, 5)]
import pdb
s.insert(test1, Interval(4, 9))
pdb.set_trace()
s.insert(test2 , Interval(6, 8))
s.insert(test2, Interval(0, 3))
