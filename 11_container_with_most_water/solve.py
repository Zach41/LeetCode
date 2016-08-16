#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        n = len(height)
        if n <= 1:
            return 0
        
        i, j = 0, n-1
        maxW = 0
        while i < j:
            h = min(height[i], height[j])
            maxW = max(maxW, (j-i)*h)
            while height[i]<=h and i < j: i+=1
            while height[j]<=h and i < j: j-=1

        return maxW

s = Solution()

print s.maxArea([3, 5, 2, 6, 5])
             
