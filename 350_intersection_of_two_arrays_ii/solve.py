#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        rec = {}

        for e in nums1:
            if rec.has_key(e):
                rec[e] += 1
            else:
                rec[e] = 1

        ans = []
        for e in nums2:
            if rec.has_key(e) and rec[e] >=1:
                ans.append(e)
                rec[e] -= 1

        return ans

s = Solution()

print s.intersect([1, 2, 2, 1], [2, 2])
        
