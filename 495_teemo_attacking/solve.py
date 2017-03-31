#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        tot = 0
        for i in range(0, len(timeSeries) - 1):
            if timeSeries[i + 1] - timeSeries[i] >= duration:
                tot += duration
            else:
                tot += timeSeries[i + 1] - timeSeries[i]
        tot += duration
        return tot


s = Solution()
print(s.findPoisonedDuration([1, 3], 2))
print(s.findPoisonedDuration([1, 2], 2))
