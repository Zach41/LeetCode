#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        if not heights:
            return 0

        stack = []
        heights.append(-1)   
        max_area = 0

        for i in range(len(heights)):
            while len(stack) != 0 and heights[i] <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] -1
                max_area = max(max_area, h*w)

            stack.append(i)
        return max_area
    

s = Solution()
import pdb
pdb.set_trace()
print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
