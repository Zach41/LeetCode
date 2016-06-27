#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rec = {}

        for e in nums1:
            if rec.has_key(e):
                continue
            rec[e] = 1
        ans = []
        for e in nums2:
            if rec.has_key(e) and not e in ans:
                ans.append(e)
        return ans

s = Solution()

print s.intersection([1, 2, 2, 1], [2, 2])
